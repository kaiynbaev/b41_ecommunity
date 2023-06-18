from django.db import models

# Create your models here.




class Login(models.Model):
    login = models.CharField(
        verbose_name = 'login',
        max_length=255,
        unique=True
    )
    password = models.CharField(
        verbose_name='password',
        max_length=255
    )
    created_date = models.DateTimeField(
        verbose_name='created_date',
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        verbose_name='updated_date',
        auto_now=True
    )
    is_block = models.BooleanField(
        verbose_name='blocked',
        default=False
    )
    def __str__(self) -> str:
        return self.login
     

#Heatlh


class SertificateForCovid_19(models.Model):
    pin = models.CharField(
        verbose_name='pin_passport',
        max_length=20,
        unique=True
    )
    passport_series = models.CharField(
        verbose_name='passport_series',
        max_length=20,
        unique=True
    )
    passport_number = models.CharField(
        verbose_name='passport_number',
        max_length=20,
        unique=True
    )
    is_exist = models.BooleanField(
        verbose_name='Имеетс] ли сертивикат',
        default=False
    )
    def __str__(self) -> str:
        return self.pin


class NarkUchet(models.Model):
    Uchet = models.BooleanField(
        verbose_name='Nark_Uchet',
        default=False
    )
    pin = models.CharField(
        verbose_name='pin_passport',
        max_length=20,
        unique=True
    )
    passport_series = models.CharField(
        verbose_name='passport_series',
        max_length=20,
        unique=True
    )
    passport_number = models.CharField(
        verbose_name='passport_number',
        max_length=20,
        unique=True
    )
    def __str__(self) -> str:
        return self.passport_number


class ZapisKVrachu(models.Model):
    client_name = models.CharField(
        verbose_name='client_name',
        max_length = 100,
        unique=True
    )
    pin = models.CharField(
        verbose_name='pin_passport',
        max_length=20,
        unique=True
    )
    Description = models.CharField(
        verbose_name='description',
        max_length=255
    )
    created_date = models.DateTimeField(
        verbose_name='created_date',
        auto_now_add=True
    )
    def __str__(self) -> str:
        return self.client_name
    

class PersonalCabinet(models.Model):
    name = models.ForeignKey(
        Login,
        on_delete=models.CASCADE
    )
    

# Education



    
