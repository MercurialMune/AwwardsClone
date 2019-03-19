from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description


class Projects(models.Model):
    project_name = models.CharField(max_length=50, blank=True)
    project_photo = models.ImageField(upload_to='projectpics/')
    description = models.TextField(blank=True)
    github_repo = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.url


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profpics/')
    bio = models.TextField(blank=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_user(self):
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
    def save_profile(sender, instance, created, **kwargs):
        user = instance
        if created:
            profile = UserProfile(user=user)
            profile.save()
