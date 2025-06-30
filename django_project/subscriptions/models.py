from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Tariff(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id}#{self.name}"


class UserSubscription(models.Model):

    tariff = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}#sub - {self.user_id}#user - {self.tariff_id}#tariff"




