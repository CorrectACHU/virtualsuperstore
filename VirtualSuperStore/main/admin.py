from django.forms import ModelChoiceField
from django.contrib import admin
from .models import *
# Register your models here.



class EarphonesAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='earphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SpeakersAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='Speakers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(EarphonesProduct, EarphonesAdmin)
admin.site.register(SpeakersProduct, SpeakersAdmin)
