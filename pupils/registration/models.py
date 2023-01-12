from django.db import models


class Region(models.Model):
    region = models.CharField(max_length=100)

    class Meta:
        db_table = 'Region'

    def __str__(self):
        return f'{self.region}'


class School_location(models.Model):
    location = models.CharField(max_length=200)

    class Meta:
        db_table = 'school location'

    def __str__(self):
        return f'{self.location}'


class Pupil(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_address = models.ManyToManyField(Region)
    studying_address = models.ManyToManyField(School_location)
    class_number = models.IntegerField()
    birth_date = models.DateField()

    class Meta:
        db_table = 'Pupil'

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'
