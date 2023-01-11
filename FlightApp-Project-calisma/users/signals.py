from django.contrib.auth.models import User # sinyali create eder
from django.db.models.signals import post_save  # sinyali gonderen
from django.dispatch import receiver # sinyali yakalayan
from rest_framework.authtoken.models import Token # yeni islem yapan


@receiver(post_save, sender=User)
def create_Token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# instance = userin gonderdigi sinyali instance ile yakalanir. 