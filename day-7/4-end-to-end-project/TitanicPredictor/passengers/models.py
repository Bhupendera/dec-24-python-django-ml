from django.db import models

class Passenger(models.Model):
    Pclass = models.IntegerField()
    Age = models.FloatField()
    SibSp = models.IntegerField()
    Parch = models.IntegerField()
    Fare = models.FloatField()
    Sex_male = models.BooleanField()
    Embarked_Q = models.BooleanField()
    Embarked_S = models.BooleanField()
    prediction = models.CharField(max_length=20)

    def __str__(self):
        return f"Passenger {self.id}: {self.prediction}"
