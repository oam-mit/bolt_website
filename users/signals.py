from django.db.models.signals import post_save,pre_delete,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
import os

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        profile=Profile(user=instance)
        profile.save()


@receiver(pre_save, sender=Profile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
        if old_file.url == '/media/default.jpg':
            return False
    except:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)