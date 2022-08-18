from django.db import models
from django.core.validators import RegexValidator

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth,phone_no,national_id, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.is_admin = False
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth,phone_no,national_id,  password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            phone_no=phone_no,
            national_id=national_id, 
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=100)
    
    date_of_birth = models.DateField(default=None, blank=True, null=True)
   
    phone_regex = RegexValidator(regex=r'(05|5)\d{8}', message="Phone number must be entered in the format: '0599909999 or 599999999'. Up to 10 digits allowed.")
    phone_no = models.CharField(validators=[phone_regex], max_length=10, blank=True) # Validators should be a list
   
    national_regex = RegexValidator(regex=r'(2|1)\d{9}', message="national number must be entered in the format: '1999909999 or 2999999999'. Up to 10 digits allowed.")
    national_id = models.CharField(validators=[national_regex], max_length=10, blank=True) # Validators should be a list
    is_active = models.BooleanField(default=True) #, blank=True, null=True)
    is_admin = models.BooleanField(default=False) #, blank=True, null=True)
   

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth','phone_no','national_id']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
