from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Address, Vendor, VendorProfile, Country, Province, VendorCategory, VendorProfilePicture, VendorPromotion, VendorPromotionPicture


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ['name']

class ProvinceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Province
        fields = ['name']

class VendorCategorySerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Province
        fields = ['name']

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    province = serializers.StringRelatedField(many=False)
    class Meta:
        model = Address
        fields = ['street_name','street_number','unit','city','zip_code','province']



class VendorProfilePictureSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = VendorProfilePicture
        fields = ['path','order']
        order_with_respect_to = "order"



class VendorProfileSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer(many=False)
    category = serializers.StringRelatedField(many=False)
    pictures = VendorProfilePictureSerializer(many=True)
    class Meta:
        model = VendorProfile
        fields = ['id','vendor_id', 'name','description','category','address','pictures']

class VendorPromotionPictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendorProfilePicture
        fields = ['path','order']
        order_with_respect_to = "order"

class VendorPromotionSerializer(serializers.HyperlinkedModelSerializer):
    pictures = VendorPromotionPictureSerializer(many=True)
    class Meta:
        model = VendorPromotion
        fields = ['id','vendor_id', 'name','description','points_required','pictures','expiration_date']

class VendorCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VendorCategory
        fields = ['name']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id','enabled']
