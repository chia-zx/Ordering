from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from app.models import Customer, Vendor, DeliveryPerson, SystemManager

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a Vendor instance when a new User is created.
    """
    if not instance.is_staff:
        if instance.groups.filter(name='Vendor').exists():
            Vendor.objects.get_or_create(
                user=instance,
                defaults={
                    'vendor_name': None,
                    'vendor_phone': None,
                    'vendor_address': None,
                    'vendor_revenue': 0.0
                }
            )

        elif instance.groups.filter(name='Customer').exists():
            # Create a Customer profile
            Customer.objects.get_or_create(
                user=instance,
                defaults={
                    'customer_name': None,
                    'customer_phone': None,
                    'customer_address': None,
                    'customer_spent': 0.0
                }
            )

        elif instance.groups.filter(name='DeliveryPerson').exists():
            # Create a DeliveryPerson profile
            DeliveryPerson.objects.get_or_create(
                user=instance,
                defaults={
                    'deliveryperson_name': None,
                    'deliveryperson_phone': None,
                    'deliveryperson_address': None
                }
            )  

        elif instance.groups.filter(name='SystemManager').exists():
            # Create a Manager profile
            SystemManager.objects.get_or_create(
                user=instance,
                defaults={
                    'manager_name': None,
                }
            )
