from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from conf import settings

env = settings.env

UserModel = get_user_model()


class Command(BaseCommand):
    """
    Command for creating a super admin using default admin credentials
    """
    def handle(self, *args, **options):
        is_exist = UserModel.objects.filter(
            username=env.str('DEFAULT_ADMIN_USERNAME')
        ).first()

        if not is_exist:
            user = UserModel.objects.create_user(
                username=env.str('DEFAULT_ADMIN_USERNAME'),
                email=env.str('DEFAULT_ADMIN_EMAIL'),
                full_name=env.str('DEFAULT_ADMIN_FULL_NAME'),
                password=env.str('DEFAULT_ADMIN_PASSWORD')
            )
            user.set_password(env.str('DEFAULT_ADMIN_PASSWORD'))
            user.is_superuser = True
            user.is_staff = True
            user.save()
            print('Default user created successfully')
