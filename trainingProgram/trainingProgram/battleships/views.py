from django.shortcuts import render, redirect
from battleships.forms import placementForm, inviteForm, shootForm
from battleships import utils
from django.contrib.auth.decorators import login_required
from .models import Game, GameUsers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import json


@login_required
def new_game(request):
    context = {}
    get_object_or_404(GameUsers, user=request.user)
    context['allUsrs'] = GameUsers.objects.exclude(user=request.user)

    pl1 = GameUsers.objects.get(user=request.user)
    pl2 = None
    if request.method == 'POST':
        p2Id = request.POST.get("p2", "")
        if p2Id:
            pl2 = GameUsers.objects.get(id=p2Id)
            currentGame = Game(player_1=pl1, player_2=pl2)
            currentGame.save()
        currentGame.gameStatus = 1
        playerData = {}
        playerData['placements'] = []
        playerData['hits'] = []
        playerData['misses'] = []
        currentGame.save()
    return render(request, "battleships/new_game.html", context)


@login_required
def games_list(request):
    context = {}
    get_object_or_404(GameUsers, user=request.user)
    currentPlayer = GameUsers.objects.get(user=request.user)
    allPl1Games = Game.objects.filter(player_1=currentPlayer)
    allPl2Games = Game.objects.filter(player_2=currentPlayer)

    context['allPl1Games'] = allPl1Games
    context['allPl2Games'] = allPl2Games
    return render(request, "battleships/games_list.html", context)


@login_required
def placeShips(request, gameId):
    currentPlayer = GameUsers.objects.get(user=request.user)
    currentGame = Game.objects.get(pk=gameId)
    playerNum = 0

    if currentGame.player_1 != currentPlayer and currentGame.player_2 != currentPlayer:
        print "ERROR"

    if currentGame.player_1 == currentPlayer:
        playerNum = 1
    elif currentGame.player_2 == currentPlayer:
        playerNum = 2

    context = {}
    ships = ['Aircraft_Carrier', 'Battleship', 'Cruiser', 'Destroyer', 'Submarine']
    shipSizes = {'Aircraft_Carrier': 5, 'Battleship': 4,
                 'Cruiser': 3, 'Destroyer': 2, 'Submarine': 1}

    shipCollisions = []  # holds just the ship names that have collided instead of every cell
    diagonalShips = []
    wrongSizeShips = []
    usedCells = []
    cellsWithShips = []
    if request.method == 'POST':
        form = placementForm(request.POST)
        if form.is_valid():
            for ship in ships:
                collision = False
                XCoord = request.POST.get(ship + "_X")
                YCoord = request.POST.get(ship + "_Y")
                X_start = XCoord[0]
                X_end = XCoord[1:]
                Y_start = YCoord[0]
                Y_end = YCoord[1:]
                shipPlacementInfo = utils.getCells(X_start, X_end, Y_start, Y_end, ship)
                success = shipPlacementInfo[0]
                cells = shipPlacementInfo[1]
                message = shipPlacementInfo[2]
                colour = shipPlacementInfo[3]

                if success:  # if successfull
                    length = len(cells)
                    if length == shipSizes[ship]:
                        for i in cells:
                            if i in usedCells:
                                shipCollisions.append(ship)  # for list of all collided ships
                                collision = True
                            else:
                                usedCells.append(i)
                            if not collision:  # only paint it if theres no collision
                                context[i] = colour  # paint the cell in specified colour
                                cellsWithShips.append(i)
                    else:
                        wrongSizeShips.append(ship)
                elif message == "diagonal":
                    diagonalShips.append(ship)

            game = Game.objects.get(pk=gameId)
            gameData = {}
            gameData['placements'] = []
            gameData['hits'] = []
            gameData['misses'] = []
            if playerNum == 1:
                gameData['placements'] = cellsWithShips
                game.player_1_data = json.dumps(gameData)
                game.gameStatus = 2
            elif playerNum == 2:
                gameData['placements'] = cellsWithShips
                game.player_2_data = json.dumps(gameData)
                game.gameStatus = 3
            game.save()
            return redirect('/lobby/' + gameId)
            # return render(request, "battleships/lobby.html", context)  # if valid go to game lobby

        context['form'] = form
        context['cellsWithShips'] = cellsWithShips
        context['wrongSizeShips'] = wrongSizeShips
        context['shipCollisions'] = set(shipCollisions)
        context['diagonalShips'] = diagonalShips
        context['lobbyId'] = gameId
        return render(request, "battleships/place.html", context)  # if not valid stay there and display errors

    else:
        form = placementForm(request.POST)
        return render(request, "battleships/place.html", {'form': form})


@login_required
def lobby(request, gameId):
    context = {}
    currentGame = Game.objects.get(pk=gameId)
    currentPlayer = GameUsers.objects.get(user=request.user)

    if currentGame.player_1 == currentPlayer:
        playerNum = 1
    elif currentGame.player_2 == currentPlayer:
        playerNum = 2

    gameStatus = currentGame.gameStatus
    gameStatusVerbose = currentGame.get_gameStatus_display()

    if currentGame.player_1_data and currentGame.player_2_data:
        player1Data = json.loads(currentGame.player_1_data)
        player1Hits = player1Data["hits"]
        player1Misses = player1Data["misses"]

        player2Data = json.loads(currentGame.player_2_data)
        player2Hits = player2Data["hits"]
        player2Misses = player2Data["misses"]

        if playerNum == 1:
            # left panel
            for i in player1Data["placements"]:
                context[i] = "yellow"

            if player2Hits:
                for i in player2Hits:
                    context[i] = "black"
            if player2Misses:
                for i in player2Misses:
                    context[i] = "green"

            #right panel
            if player1Hits:
                for i in player1Hits:
                    coord = 'r' + i
                    context[coord] = "red"
            if player1Misses:
                for i in player1Misses:
                    coord = 'r' + i
                    context[coord] = "blue"

        if playerNum == 2:
            if player2Hits:
                for i in player2Data["placements"]:
                    context[i] = "yellow"
                if player1Hits:
                    for i in player1Hits:
                        context[i] = "black"
                if player1Misses:
                    for i in player1Misses:
                        context[i] = "green"

            if player2Hits:
                for i in player2Hits:
                    coord = 'r' + i
                    context[coord] = "red"

            if player2Misses:
                for i in player2Misses:
                    coord = 'r' + i
                    context[coord] = "blue"

    context['lobbyId'] = gameId
    context['gameStatus'] = gameStatus
    context['gameStatusVerbose'] = gameStatusVerbose
    context['playerNum'] = playerNum

    context['refreshable'] = True


    return render(request, "battleships/lobby.html", context)


def shoot(request, gameId):
    context = {}
    currentGame = Game.objects.get(pk=gameId)
    currentPlayer = GameUsers.objects.get(user=request.user)

    if request.method == 'POST':
        if currentGame.gameStatus == 6:
            pass
        form = shootForm(request.POST)
        if form.is_valid():
            coord = request.POST.get("coord")

            hits = []
            misses = []
            if currentGame.player_1 == currentPlayer:
                player1Data = json.loads(currentGame.player_1_data[0:])
                hits = player1Data["hits"]
                misses = player1Data["misses"]

                if coord in player1Data["placements"]:
                    hits.append(coord)
                else:
                    misses.append(coord)

                if len(hits) >= 15:
                    currentGame.gameStatus = 6
                    currentGame.winner = currentPlayer
                    pass

                currentGame.next_to_move = currentGame.player_2
                currentGame.gameStatus = 4

                playerData = {}
                playerData['placements'] = player1Data["placements"]
                playerData['hits'] = hits
                playerData['misses'] = misses
                currentGame.player_1_data = json.dumps(playerData)

            elif currentGame.player_2 == currentPlayer:
                player2Data = json.loads(currentGame.player_2_data[0:])
                hits = player2Data["hits"]
                misses = player2Data["misses"]
                if coord in player2Data["placements"]:
                    hits.append(coord)
                else:
                    misses.append(coord)

                if len(hits) >= 15:
                    currentGame.gameStatus = 6
                    currentGame.winner = currentPlayer
                    pass

                currentGame.next_to_move = currentGame.player_1
                currentGame.gameStatus = 3

                playerData = {}
                playerData['placements'] = player2Data["placements"]
                playerData['hits'] = hits
                playerData['misses'] = misses
                currentGame.player_2_data = json.dumps(playerData)

            currentGame.save()

            return redirect('/lobby/' + gameId)

    else:
        form = shootForm(request.POST)

    """
    if im player 1 and waiting for player 2 to shooot, do refresh
    otherwise stay on page
    
    if im player 2 and waiting for player 1 to shoot, do refresh
    otherwise stay on page
    """


    if currentGame.player_1 == currentPlayer:
        player1Data = json.loads(currentGame.player_1_data[0:])
        for i in player1Data["hits"]:
            context[i] = "red"
        for i in player1Data["misses"]:
            context[i] = "blue"
    elif currentGame.player_2 == currentPlayer:
        player2Data = json.loads(currentGame.player_2_data[0:])
        for i in player2Data["hits"]:
            context[i] = "red"
        for i in player2Data["misses"]:
            context[i] = "blue"

    context['form'] = form
    context['currentPlayer'] = currentPlayer
    return render(request, "battleships/shoot.html", context)
