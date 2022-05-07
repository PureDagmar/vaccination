from django.db import models


# Create your models here.
class Client(models.Model):
    GENDER = (
        ("M", "Male"),
        ('F', "Female"),
    )
    name = models.CharField(max_length=300)
    birth_date = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    mother_name = models.CharField(max_length=300)
    phone = models.IntegerField(help_text="+7(999)999-99-99")
    town = models.CharField(max_length=300)
    compound = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Vaccine(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
