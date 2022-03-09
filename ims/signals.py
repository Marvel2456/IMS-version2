from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from .models import Staff

@receiver(post_save, sender=User)
def staff_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='staff')
        instance.groups.add(group)
        Staff.objects.create(user=instance, name=instance.username)