from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **other_fields):
        return self.create_user(email, password, is_admin=True, **other_fields)
