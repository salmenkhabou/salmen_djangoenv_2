from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.

class produit(models.Model):
    TYPE_CHOICES=[
        ('em','emballé'),
        ('fr','Frais'),
        ('cs','Conserve')
    ]
    libellé=models.CharField(max_length=100)
    description=models.TextField(default='Non définie')
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True,upload_to='media/')
    categorie=models.ForeignKey('categorie',on_delete=models.CASCADE,null=True)
    fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "libellé "+self.libellé+" description "+self.description+" prix "+str(self.prix)+" type "+self.type
class categorie(models.Model):
    TYPE_CHOICES=[
        ('al','alimentaire'),
        ('mb','meuble'),
        ('vs','vaisselle'),
        ('sn','sanitaire'),
        ('vt','vetement'),
        ('jx','jouets'),
        ('lg','linge de maison'),
        ('bj','bijoux'),
        ('dc','decor')

    ]
    libellé=models.CharField(default='al',choices=TYPE_CHOICES,max_length=50)
    def __str__(self):
        return self.libellé
class fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField(default='Non définie')
    email=models.EmailField(default='Non définie')
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.nom
class produitNC(produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return "libellé "+self.libellé+" description "+self.description+" prix "+str(self.prix)+" type "+self.type+" duree de garantie "+self.Duree_garantie
class command(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('produit')	
#panier
# """
# class User(AbstractUser):
#     email = models.EmailField(blank=True, unique=True)
#     adresse = models.CharField(max_length=255, blank=True)
#     ville = models.CharField(max_length=255, blank=True)
#     code_postal = models.CharField(max_length=10, blank=True)

#     #USERNAME_FIELD = 'username'
#     #REQUIRED_FIELDS = ['email']

#     def __str__(self):
#         return self.username

# class Panier(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     produit = models.ForeignKey(produit, on_delete=models.CASCADE)
#     quantite = models.PositiveIntegerField(default=1)
#     prix_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

# class LigneCommande(models.Model):
#     commande = models.ForeignKey(command, on_delete=models.CASCADE, related_name='lignes_commande')
#     produit = models.ForeignKey(produit, on_delete=models.CASCADE)
#     quantite = models.PositiveIntegerField(default=1)
#     prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
#     prix_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

#     def save(self, *args, **kwargs):
#         self.prix_total = self.quantite * self.prix_unitaire
#         super().save(*args, **kwargs)"""
