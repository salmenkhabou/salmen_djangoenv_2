from rest_framework.serializers import ModelSerializer
 
from magasin.models import *
 
class CategorySerializer(ModelSerializer):
 
    class Meta:
        model = categorie
        fields = "__all__"

class ProduitSerializer(ModelSerializer):
 
    class Meta:
        model = produit
        fields = "__all__"

