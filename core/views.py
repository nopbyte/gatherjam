
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from core.serializers import UserSerializer, GroupSerializer, VendorSerializer, VendorProfileSerializer, VendorPromotionSerializer, VendorPromotionPictureSerializer,  VendorProfilePictureSerializer, VendorCategorySerializer
from core.models import Vendor, VendorProfilePicture, VendorPromotionPicture, VendorProfile, VendorPromotion, VendorCategory,NFCTag, Address, Province, Country

import logging

logger = logging.getLogger()

class SelfViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Get UserInfo for the authenticated
        """
        user = self.request.user
        return User.objects.filter(id=user.id)

#TODO: review access acctions https://www.django-rest-framework.org/api-guide/viewsets/#introspecting-viewset-actions

class VendorCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VendorCategory.objects.all().order_by('name')
    serializer_class = VendorCategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class VendorProfilePictureViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VendorProfilePictureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        vendor_profile_id =  self.request.query_params.get('vendor_profile_id')

        if vendor_profile_id:
            queryset = VendorProfilePicture.objects.filter(vendor_profile_id=vendor_profile_id)
        else:
            queryset = VendorProfilePicture.objects.all().order_by('order')
        return queryset

class VendorPromotionPictureViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = VendorPromotionPictureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        vendor_promotion_id =  self.request.query_params.get('vendor_promotion_id')

        if vendor_promotion_id:
            queryset = VendorPromotionPicture.objects.filter(vendor_promotion_id=vendor_promotion_id).order_by('order')
        else:
            queryset = VendorPromotionPicture.objects.all().order_by('order')
        return queryset


#class VendorPromotionPictureViewSet(viewsets.ReadOnlyModelViewSet):
#    queryset = VendorPromotionPicture.objects.all().order_by('last_updated')
#    serializer_class = VendorPromotionPictureSerializer
#    permission_classes = [permissions.IsAuthenticated]


class VendorProfileViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = VendorProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        category_names =  self.request.query_params.getlist('category','')
        result = []
        try:
            if category_names:
                for category_name in category_names:
                    logger.info('got category name: {}'.format(category_name))
                    try:
                        category = VendorCategory.objects.get(name = category_name)
                        new_stuff = VendorProfile.objects.filter(category=category).order_by('name')
                        logger.info('got {} vendor profiles based on category {}'.format(len(new_stuff),category_name))
                        result.extend(new_stuff)

                    except Exception as e:
                        logger.debug('get for category had exception {}'.format(type(e)))
                return result
            return VendorProfile.objects.all().order_by('name')
        except Exception as e:
            logger.warning('unexpected error in view: {}'.format(type(e)))
            return VendorProfile.objects.all().order_by('name')

class VendorPromotionViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = VendorPromotion.objects.all().order_by('name')
    serializer_class = VendorPromotionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        try:
            vendor_id = self.request.query_params.get('vendor_id')
            if vendor_id is not None:
                try:
                    vendor = Vendor.objects.get(id=vendor_id)
                    return VendorPromotion.objects.filter(vendor=vendor).order_by('name')
                except Exception as e:
                    logger.debug('get for vendor by id {} had exception {}'.format(vendor_id, type(e)))
                    return []
        except Exception as e:
            logger.warning('unexpected error in view: {}'.format(e))
        return VendorPromotion.objects.all().order_by('name')




class VendorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = VendorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        enabled =  self.request.query_params.get('enabled')
        if enabled is not None:
            return Vendor.objects.filter(enabled=enabled).order_by('email')
        return Vendor.objects.all().order_by('email')



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]