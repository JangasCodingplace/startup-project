from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from assets.helper import generate_key
from django.template.defaultfilters import slugify


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a normal user.
        """

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """
        Creates and saves a superuser.
        """
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    key = models.CharField(
        _("Key"),
        max_length=8,
        primary_key=True,
        editable=False
    )
    url_arg = models.CharField(
        _("URL Argument"),
        max_length=100,
        unique=True,
        editable=False,
        db_index=True
    )
    email = models.EmailField(
        _("Email"),
        max_length=255,
        unique=True,
        db_index=True
    )
    first_name = models.CharField(
        _("First Name"),
        max_length=40,
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=40
    )
    is_admin = models.BooleanField(
        _("Is Admin"),
        default=False
    )
    is_active = models.BooleanField(
        _("Is Active"),
        default=True,
        help_text="This blocks for login.\
                   The user has no influence on that."
    )
    is_activated_by_key = models.BooleanField(
        _("Is activated by key"),
        default=False,
        help_text="This is a user side activation via Email."
    )
    registration_date = models.DateTimeField(
        _("Registration Date"),
        auto_now_add=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]
    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ("-registration_date", )

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.pk:
            self.key = generate_key(length=8, model=User)
            self.__set_user_arg()

        super().save(*args, **kwargs)

    def __set_user_arg(self):
        first_name = slugify(self.first_name).replace('-', '')
        last_name = slugify(self.last_name).replace('-', '')
        url_arg = f"{first_name}-{last_name}"
        users = User.objects.filter(url_arg__startswith=url_arg)
        user_arg_count = users.count()
        if user_arg_count > 1:
            newest_user = users.order_by('url_arg').last()
            new_index = int(newest_user.url_arg.split('-')[-1])
            self.url_arg = f"{url_arg}-{new_index + 1}"
        elif user_arg_count > 0:
            self.url_arg = f"{url_arg}-2"
        else:
            self.url_arg = f"{url_arg}"

    def has_perm(self, perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, Auth):
        # "Does the user have permissions to view the app Auth?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
