from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, full_name, email, password, **extra_fields):
        """
        Manager method for creating new user
        @param username: Username of user
        @param full_name: Full name of user
        @param email: email address of user
        @param password: Password of user
        @param extra_fields: Extra information
        @return: Newly created user object
        """
        if not username:
            raise ValueError('Username must be required')
        if not full_name:
            raise ValueError('Full name must be required')
        if not email:
            raise ValueError('Email must be required')

        email = self.normalize_email(email)
        user = self.model(username=username, full_name=full_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, email, password=None):
        """
        Manager model for creating superuser
        @param username: Username of user
        @param full_name: Full name of user
        @param email: email address of user
        @param password: Password of user
        @return: Newly created user object
        """
        email = self.normalize_email(email)
        user = self.create_user(username=username, full_name=full_name, email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
