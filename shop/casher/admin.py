from django.contrib import admin

# Register your models here.

from .models import Revealed, Total


class RevealedAdmin(admin.ModelAdmin):
    model = Revealed
    list_display = ['date', 'name', 'given', 'reminder', 'docName', 'revealDate', 'paName']


class TotalAdmin(admin.ModelAdmin):
    model = Total
    list_display = ['total']


admin.site.register(Revealed, RevealedAdmin)
admin.site.register(Total, TotalAdmin)
