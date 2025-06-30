from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Order(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.id}#order - {self.owner_id}#user"
