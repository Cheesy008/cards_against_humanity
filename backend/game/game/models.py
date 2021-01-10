from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Game(models.Model):
    players = models.ManyToManyField(User,
                                     related_name='players_game_set')
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                related_name='creator_game_set')

    def __str__(self):
        return self.name


class Round(models.Model):
    pass
