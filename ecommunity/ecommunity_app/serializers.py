from rest_framework import serializers
from .models import Login, SertificateForCovid_19, NarkUchet, ZapisKVrachu

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'
        
class SertificateForCovid_19Serializer(serializers.ModelSerializer):
    class Meta:
        model = SertificateForCovid_19
        fields = '__all__'
        
class NarkUchetSerializer(serializers.ModelSerializer):
    class Meta:
        model = NarkUchet
        fields = '__all__'
        
class ZapisKVrachuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZapisKVrachu
        fields = '__all__'