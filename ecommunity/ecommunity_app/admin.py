from django.contrib import admin
from .models import Login, SertificateForCovid_19, NarkUchet, ZapisKVrachu
# Register your models here.

class LoginAdmin(admin.ModelAdmin):
    list_display = ('verbose_name', )

class NarkUchetAdmin(admin.ModelAdmin):
    list_display = ('pin', 'Uchet')
    



admin.site.register(Login)
admin.site.register(SertificateForCovid_19)
admin.site.register(NarkUchet, NarkUchetAdmin)
admin.site.register(ZapisKVrachu)
3


