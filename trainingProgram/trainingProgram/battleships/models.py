from django.contrib.auth.models import User
from django.db import models

class GameUsers(models.Model):
    user = models.ForeignKey(User)
    username = models.TextField(blank = True, null = True)
    firstname = models.TextField(blank = True, null = True)
    lastname = models.TextField(blank = True, null = True)
    emailAdress = models.TextField(blank = True, null = True)
    createdDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updatedDate = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str("%s" % self.username)
#
class Game(models.Model):
    GAME_STATUSES = (
        (0, 'Active'),
        (1, 'Waiting for player 1 to set up'),
        (2, 'Waiting for player 2 to set up'),
        (3, 'Waiting for player 1 to shoot'),
        (4, 'Waiting for player 2 to shoot'),
        (5, 'Abandoned'),
        (6, 'Finished'),
        (7, 'Waiting for players to join'),
    )

    winner = models.ForeignKey(GameUsers, blank = True, null = True, db_index = True)
    player_1 = models.ForeignKey(GameUsers, related_name = "game_player_1", blank = True, null = True, db_index = True)
    player_1_data = models.TextField(blank=True,null=True)
    player_2 = models.ForeignKey(GameUsers, related_name = "game_player_2", blank = True, null = True)
    player_2_data = models.TextField(blank=True,null=True)
    next_to_move = models.ForeignKey(GameUsers, related_name="game_next_to_move", blank = True, null = True)
    start_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, db_index=True)
    gameStatus = models.IntegerField(null = True, blank = True, default = '5', choices = GAME_STATUSES, db_index = True)

    def __str__(self):
        return "{0} vs {1}, id = {2}".format(self.player_1, self.player_2, self.pk)
