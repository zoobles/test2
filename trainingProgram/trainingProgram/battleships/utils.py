import string

def getCells(X_start,X_end, Y_start,Y_end, ship):
    colour = getColour(ship)
    sameColumn = False;
    sameRow = False;
    diagonal = False;
    success = False;
    cells = [] #list of cells between x,y coordinates
    message = ''

    if string.lowercase.index(X_start) == string.lowercase.index(Y_start):
        sameColumn = True
    if X_end == Y_end:
        sameRow = True
    if not sameColumn and not sameRow:
        diagonal = True;

    if sameColumn:
        column = X_start #first letter of the coordinate
        for i in range (int(X_end), int(Y_end) +1):
            row = str(i)
            cells.append(column + row)

    elif sameRow:
        alpha = string.lowercase
        row = X_end
        for i in range (string.lowercase.index(X_start), string.lowercase.index(Y_start) +1):
            column = alpha[i]
            cells.append(column + row)

    if cells:
        success = True
    else:
        message = "empty"

    if diagonal:
        message = "diagonal"


    return success, cells, message, colour

def getColour(ship):
    if ship == "Aircraft_Carrier": return "red"
    if ship == "Battleship": return "yellow"
    if ship == "Cruiser": return "blue"
    if ship == "Destroyer": return "orange"
    if ship == "Submarine": return "green"
