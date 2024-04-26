from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

User = get_user_model()

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField(
        'image',
        default='placeholder',
        transformation=[{'width':500, 'height':500, 'crop':'auto'}]
    )
    
    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
