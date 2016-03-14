from django.contrib import admin
from popular.models import Places, DetailPlaces
from featured.models import Feature, DetailFeature
from contact.models import User
# Register your models here.

admin.site.register(Places)
admin.site.register(DetailPlaces)
admin.site.register(Feature)
admin.site.register(DetailFeature)
admin.site.register(User)