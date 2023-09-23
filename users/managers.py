from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """Класс для реализации добавления superuser."""
    def create_user(self, email, password):

        if not email:
            raise TypeError(
                'У пользователей должен быть адрес электронной почты.')

        if not password:
            raise TypeError('У пользователей должен быть пароль.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
