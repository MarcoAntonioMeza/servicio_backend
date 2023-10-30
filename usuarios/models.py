from django.db import models

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin , Group

# Create your models here.

class UserManager(BaseUserManager):
    
    def _create_user(self,username,email,name,last_name,password,is_staff,is_superuser,**extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user
    
    #def create_user(self, username, email, name,last_name, password=None, **extra_fields):
     #   return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)



class Usuario(AbstractBaseUser,PermissionsMixin):

    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    #image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    direccion = models.CharField(max_length=255, blank=True)
    numero_telefono = models.CharField(max_length=15, blank=True)
    #ciudad = models.CharField(max_length=100, blank=True)
    TIPO_USUARIO = [
        ('Administrador', 'Administrador'),
        ('Técnico', 'Técnico'),
        ('Cliente', 'Cliente'),
    ]
    tipo = models.CharField(max_length=30, choices=TIPO_USUARIO)

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'


    def __str__(self):
        return f'{self.name} {self.last_name}'
    
    #def save(self, *args, **kwargs):
     #   user = super(Usuario, self).save( *args, **kwargs)