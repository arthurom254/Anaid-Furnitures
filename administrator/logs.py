#logs
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import YourModel, ActivityLog

@receiver(pre_save, sender=YourModel)
def pre_save_activity(sender, instance, **kwargs):
    # This function is called before saving the model
    # Perform any actions or manipulations you want here
    pass

@receiver(post_save, sender=YourModel)
def post_save_activity(sender, instance, created, **kwargs):
    # This function is called after saving the model
    # You can log the activity in a separate model or perform any other actions

    if created:
        # New object is created b
        log = ActivityLog(model_name=sender.__name__, action="Created")
    else:
        # Existing object is updated
        log = ActivityLog(model_name=sender.__name__, action="Updated")
        log.save()