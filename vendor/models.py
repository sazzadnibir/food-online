from django.db import models
from accounts.models import User, UserProfile


class Vendor(models.Model):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    user_profile = models.OneToOneField(UserProfile, related_name="userprofile", on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=100, blank=True, null=True)
    vendor_license = models.ImageField(upload_to="vendor/license", blank=True, null=True)
    is_approved = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name
