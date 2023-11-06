from django.contrib import admin
from .models import Company, PriceBid, Part, Test

admin.site.register(Company)
admin.site.register(PriceBid)
admin.site.register(Part)
admin.site.register(Test)
