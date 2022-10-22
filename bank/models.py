from django.db import models
from users.models import User

class Comptesespece(models.Model):
    idclient = models.ForeignKey(User, on_delete=models.CASCADE)
    datecreation = models.DateTimeField(db_column='DateCreation', blank=True, null=True)  
    web = models.CharField(db_column='Web', blank=True, null=True,max_length=255)  
    etat = models.CharField(db_column='Etat', blank=True, null=True,max_length=255)  

class Imputationsespeces(models.Model):
    idcompteespece = models.ForeignKey(Comptesespece, on_delete=models.CASCADE)  
    montant = models.FloatField(db_column='Montant', blank=True, null=True) 
    sens = models.IntegerField(db_column='Sens', blank=True, null=True)  
    dateimputation = models.DateTimeField(db_column='DateImputation', blank=True, null=True)  
    iddateimputation = models.IntegerField(db_column='IdDateImputation', blank=True, null=True)    
    datevaleur = models.DateTimeField(db_column='DateValeur', blank=True, null=True)  
    nature = models.CharField(db_column='Nature', blank=True, null=True,max_length=255)  
    etat = models.IntegerField(db_column='Etat', blank=True, null=True)  
    dateetat = models.DateTimeField(auto_now_add=True)  
    libelle = models.TextField(blank=True, null=True,max_length=255)  


