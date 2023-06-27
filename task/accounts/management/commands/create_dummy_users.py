from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.models import auth


class Command(BaseCommand):
    help = 'Creates dummy users with custom passwords'

    def handle(self, *args, **options):
        User = get_user_model()

        # Create the admin user
        admin_user = User.objects.create_user(username='admin', email='admin@example.com', password='admin')
        authinstance=auth.objects.create(user=admin_user,is_admin=True)
        
        admin_user.save()
        authinstance.save()

        # Create customer1 user
        customer1_user = User.objects.create_user(username='customer1', email='customer1@example.com', password='customer1')
        authinstance2=auth.objects.create(user=customer1_user,is_admin=False)
        
        customer1_user.save()
        authinstance2.save()

        # Create customer2 user
        customer2_user = User.objects.create_user(username='customer2', email='customer2@example.com', password='customer2')
        
        authinstance3=auth.objects.create(user=customer2_user,is_admin=False)
        
        customer2_user.save()
        authinstance3.save()

        self.stdout.write(self.style.SUCCESS('Dummy users created successfully.'))
