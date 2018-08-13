from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name = "名字"
    )
    heat = models.IntegerField(
        default=0
    )
    def __str__(self):
        return self.name
