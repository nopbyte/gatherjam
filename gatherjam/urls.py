
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'self', views.SelfViewSet, basename='self')

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'vendor', views.VendorViewSet, basename='vendor')
router.register(r'vendor_profile', views.VendorProfileViewSet, basename='vendor_profile')
router.register(r'vendor_promotion', views.VendorPromotionViewSet)
router.register(r'categories', views.VendorCategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]


