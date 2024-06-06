from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from authentication.models import Profile
from home.models import Joke, ReportedJoke, Notification

ignore = False

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, username=instance.username)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=Profile)
def ifBanned(sender, instance, **kwargs):
    if instance.isBanned:
        Joke.objects.filter(from_user=instance.user.username).delete()
        ReportedJoke.objects.filter(from_user=instance.user.username).delete()
        Notification.objects.filter(for_user=instance.user.username).delete()

@receiver(pre_delete, sender = User)
def ifDeleted(sender, instance, **kwargs):
    Joke.objects.filter(from_user=instance.username).delete()
    ReportedJoke.objects.filter(from_user=instance.username).delete()
    Notification.objects.filter(for_user=instance.username).delete()

@receiver(pre_delete, sender=Joke)
def deleteJoke(sender, instance, **kwargs):
    global ignore
    ignore = True
    ReportedJoke.objects.filter(joke_id=instance.id).delete()


@receiver(pre_delete, sender=ReportedJoke)
def deleteSameReports(sender, instance, **kwargs):
    global ignore
    if not ignore:
        ignore = True
        ReportedJoke.objects.filter(joke_id=instance.joke_id).delete()
