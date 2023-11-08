from django.db import models

class Cordinate(models.Model):
    x = models.CharField(max_length=300)
    y = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.x}, {self.y}"

    class Meta:
        verbose_name = "Yetkazib beruvchi kardinatasi"
        verbose_name_plural = "Yetkazib beruvchi kardinatasi"