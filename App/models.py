# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clients(models.Model):
    idpersonne = models.IntegerField(db_column='IdPersonne', blank=True, null=True)  # Field name made lowercase.
    idclasse = models.IntegerField(db_column='IdClasse', blank=True, null=True)  # Field name made lowercase.
    idnatureidt = models.IntegerField(db_column='IdNatureIdt', blank=True, null=True)  # Field name made lowercase.
    idpays = models.IntegerField(db_column='IdPays', blank=True, null=True)  # Field name made lowercase.
    natureclient = models.CharField(db_column='NatureClient', blank=True, null=True)  # Field name made lowercase.
    etat = models.CharField(db_column='Etat', blank=True, null=True)  # Field name made lowercase.
    idcategorieavoir = models.IntegerField(db_column='IdCategorieAvoir', blank=True, null=True)  # Field name made lowercase.
    raisonsociale = models.TextField(db_column='RaisonSociale', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    matricule = models.TextField(db_column='Matricule', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Clients'


class Comptesespece(models.Model):
    idcompte = models.IntegerField(db_column='IdCompte', blank=True, null=True)  # Field name made lowercase.
    idclient = models.IntegerField(db_column='IdClient', blank=True, null=True)  # Field name made lowercase.
    iddepositaire = models.IntegerField(db_column='IdDepositaire', blank=True, null=True)  # Field name made lowercase.
    datecreation = models.DateTimeField(db_column='DateCreation', blank=True, null=True)  # Field name made lowercase.
    web = models.CharField(db_column='Web', blank=True, null=True)  # Field name made lowercase.
    etat = models.CharField(db_column='Etat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ComptesEspece'


class Imputationsespeces(models.Model):
    idimputation = models.IntegerField(db_column='IdImputation', blank=True, null=True)  # Field name made lowercase.
    idcompteespece = models.IntegerField(db_column='IdCompteEspece', blank=True, null=True)  # Field name made lowercase.
    montant = models.TextField(db_column='Montant', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sens = models.IntegerField(db_column='Sens', blank=True, null=True)  # Field name made lowercase.
    dateimputation = models.DateTimeField(db_column='DateImputation', blank=True, null=True)  # Field name made lowercase.
    iddateimputation = models.IntegerField(db_column='IdDateImputation', blank=True, null=True)  # Field name made lowercase.
    idsdbcompte = models.IntegerField(db_column='IdSDBCompte', blank=True, null=True)  # Field name made lowercase.
    datevaleur = models.DateTimeField(db_column='DateValeur', blank=True, null=True)  # Field name made lowercase.
    iddatevaleur = models.IntegerField(db_column='IdDateValeur', blank=True, null=True)  # Field name made lowercase.
    nature = models.CharField(db_column='Nature', blank=True, null=True)  # Field name made lowercase.
    etat = models.IntegerField(db_column='Etat', blank=True, null=True)  # Field name made lowercase.
    dateetat = models.DateTimeField(db_column='DateEtat', blank=True, null=True)  # Field name made lowercase.
    libelle = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ImputationsEspeces'
