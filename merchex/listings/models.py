from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP="HH"
        SYNTH_POP="SP"
        ALTERNATIVE_ROCK="AR"
        R_AND_B="R&B"
        AMAPIANO="AMP"
        GOSPEL="GP"
        COUPE_DECALE="CD"

    name = models.fields.CharField(max_length=100) #À cet attribut, nous attribuons un CharField, qui est l'abréviation de Character Field. Il s'agira d'un champ qui stocke des données de type caractère/texte/chaîne,
    #ce qui est le type de données approprié pour un nom.
    genre =models.fields.CharField(max_length=50)
    bibliography=models.fields.CharField(max_length=1000)
    year_formed=models.fields.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2024)]
    )
    active=models.fields.BooleanField(default=True)
    official_homepage=models.fields.URLField(null=True,blank=True)
    genre=models.fields.CharField(choices=Genre.choices,max_length=5)
    # like_new=models.fields.BooleanField(default=False)

    def  __str__(self):
        
        return f'{self.name}'

class Listing(models.Model):

    class Type(models.TextChoices):
        RECORDS="RC"
        CLOTHING="CT"
        POSTERS="PT"
        MISCELLANEOUS="MSLN"

    title=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=10000)
    sold=models.fields.BooleanField(default=False)
    year=models.fields.IntegerField()
    type=models.fields.CharField(choices=Type.choices,max_length=5)
    band=models.ForeignKey(Band,null=True,on_delete=models.SET_NULL)