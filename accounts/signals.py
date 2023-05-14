from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def poast_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        # print("create the user profile")
        UserProfile.objects.create(user=instance)
        print("User profile is created")
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the user profile if not exists
            UserProfile.objects.create(user=instance)
            # print("Profile was not exists, but I created one")

        # print("User is updated")
    

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass
    # print(instance.username, "this user is being saved")

# post_save.connect(poast_save_create_profile_receiver, sender=User)