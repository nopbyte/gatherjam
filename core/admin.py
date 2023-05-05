from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Vendor,VendorCategory,VendorProfile,VendorProfilePicture,VendorPromotion, Address, Province, Country, VendorPromotionPicture

admin.site.register(Vendor)
admin.site.register(VendorCategory)
admin.site.register(VendorProfile)
admin.site.register(VendorProfilePicture)
admin.site.register(VendorPromotionPicture)
admin.site.register(VendorPromotion)
admin.site.register(Address)
admin.site.register(Country)
admin.site.register(Province)
