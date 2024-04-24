from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='soda-hackathon/profile', default='../default_profile_lcovgw'
    )

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
