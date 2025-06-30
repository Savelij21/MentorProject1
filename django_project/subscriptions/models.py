from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Tariff(models.Model):
    name = models.CharField(max_length=50)


class UserSubscription(models.Model):

    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)




