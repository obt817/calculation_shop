from django.db import models


class day(models.Model):
    day = models.CharField(
        max_length=255,)

    def __str__(self):
        return self.day


class time(models.Model):
    time = models.CharField(
        max_length=255,)

    def __str__(self):
        return self.time


class arubaito_name(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,)

    def __str__(self):
        return self.name


class shift(models.Model):
    name = models.ForeignKey(
        arubaito_name,
        on_delete=models.CASCADE)

    Days = models.CharField(
        max_length=255,)

    Times = models.CharField(
        max_length=255,)

    day_time = models.CharField(
        max_length=255,
        unique=True,)

    def save(self, *args, **kwargs):
        self.day_time = str(str(self.Days) + str(self.Times))
        super() .save(*args, **kwargs)

    def __str__(self):
        return str(self.name)
