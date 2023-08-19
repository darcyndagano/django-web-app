from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        RAP = 'RP'

    genre = models.fields.CharField(choices=Genre.choices, max_length=5)

class Listing(models.Model):
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)])
    type = models.fields.CharField(max_length=50)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f'{self.title}'
    class Type(models.TextChoices):
        RECORDS = 'RCS'
        CLOTHING = 'CTG'
        POSTERS = 'PTS'
        MISCELLANEOUS = 'MCS'

    type = models.fields.CharField(choices=Type.choices, max_length=10)

