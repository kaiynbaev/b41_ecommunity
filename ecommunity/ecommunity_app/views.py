from .models import Login, SertificateForCovid_19, NarkUchet, ZapisKVrachu
from rest_framework import viewsets
from .serializers import (LoginSerializer, SertificateForCovid_19Serializer, NarkUchetSerializer, 
                          ZapisKVrachuSerializer)

# Create your views here.

class APILogin(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    
    
class APISertificateForCovid_19(viewsets.ModelViewSet):
    queryset = SertificateForCovid_19.objects.all()
    serializer_class = SertificateForCovid_19Serializer
    
    
class APINarkUchet(viewsets.ModelViewSet):
    queryset = NarkUchet.objects.all()
    serializer_class = NarkUchetSerializer
    
    
class APIZapisKVrachu(viewsets.ModelViewSet):
    queryset = ZapisKVrachu.objects.all()
    serializer_class = ZapisKVrachuSerializer
    
    
    
