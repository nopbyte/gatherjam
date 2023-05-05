from django.db import models

class AbstractBaseModel(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Customer(AbstractBaseModel):
    public_key = models.CharField(max_length=3000)
    #has the email been verified
    verified = models.BooleanField(default=False)
    #whether the profile is enabled or not
    enabled = models.BooleanField(default=True)


# Create your models here.
class Vendor(AbstractBaseModel):
    email = models.CharField(max_length=320)
    public_key = models.CharField(max_length=3000)
    #has the email been verified
    verified = models.BooleanField(default=False)
    #whether the profile is enabled or not
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class VendorCategory(AbstractBaseModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Country(AbstractBaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Province(AbstractBaseModel):
    country = models.ForeignKey( "Country",
                                 on_delete=models.PROTECT)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class AbstractPicture(AbstractBaseModel):
    path = models.CharField(max_length=4096)

    order = models.IntegerField()

    def __str__(self):
        return self.path

    class Meta:
        abstract = True

class Address(AbstractBaseModel):
    street_name = models.CharField(max_length=200)
    street_number = models.CharField(max_length=200)
    unit = models.CharField(null=True, blank=True, max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    province = models.ForeignKey("Province", on_delete=models.PROTECT)



class VendorProfilePicture(AbstractPicture):
    vendor_profile = models.ForeignKey(
        "VendorProfile",
        related_name='pictures',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.path


class VendorPromotionPicture(AbstractPicture):
    vendor_promotion = models.ForeignKey(
        "VendorPromotion",
        related_name='pictures',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.path

class VendorProfile(AbstractBaseModel):
    vendor = models.ForeignKey(
        "Vendor",
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        "VendorCategory",
        on_delete=models.PROTECT,
    )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    #vendorPicture_set

    def __str__(self):
        return self.name




class VendorPromotion(AbstractBaseModel):
    vendor = models.ForeignKey(
        "Vendor",
        on_delete=models.CASCADE,
    )
    enabled = models.BooleanField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    #PromotionPicture_set
    points_required = models.IntegerField()
    expiration_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name



class ClaimedPromotion(AbstractBaseModel):
    vendor_promotion = models.ForeignKey(
        "VendorPromotion",
        on_delete=models.PROTECT,
    )


class Point(AbstractBaseModel):
    vendor = models.ForeignKey(
        "Vendor",
        on_delete=models.PROTECT
    )
    customer = models.ForeignKey(
        "Customer",
        on_delete=models.PROTECT
    )

    time_of_creation = models.DateTimeField(auto_now_add=True)

    tag_value = models.CharField(max_length=200)

    claimed_promotion = models.ForeignKey(
        "ClaimedPromotion",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )


class NFCTag(AbstractBaseModel):
    vendor  = models.ForeignKey(
        "Vendor",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    serial = models.CharField(max_length=200)
    current_value = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

