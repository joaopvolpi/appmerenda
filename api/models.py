from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

class Endereco(models.Model):
    bairro = models.CharField(max_length=200)
    rua = models.CharField(max_length=300)
    numero = models.IntegerField(default=False)
    apart = models.IntegerField(default=False)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True) 
    is_staff = models.BooleanField(_('staff'), default=False)
    foto_rosto = models.ImageField(blank=True,null=True,upload_to="fotos")#dps mudar null=False
    foto_frente = models.ImageField(blank=True,null=True,upload_to="fotos")#dps mudar null=False
    foto_tras = models.ImageField(blank=True,null=True,upload_to="fotos")#dps mudar null=False
    tel = models.CharField(_('tel'), max_length=14, blank=False)
    quero_doar = models.BooleanField(default=False)

    #endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel', 'foto_rosto', 'foto_frente', 'foto_tras', 'quero_doar']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

'''
Pra referenciar o user

from django.db import models
from django.conf import settings

- O campo

tutor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
'''

