from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Usuario


@receiver(post_save, sender=Usuario)
def add_user_group(sender, instance, created, **kwargs):
    print(instance._state)
    if created: 
        user_group = None
        if instance.tipo == 'Técnico':
            user_group, _ = Group.objects.get_or_create(name='TECNICO')
        elif instance.tipo == 'Cliente':
            user_group, _ = Group.objects.get_or_create(name='CLIENTE')
        elif instance.tipo == 'Administrador':
            user_group, _ = Group.objects.get_or_create(name='ADMINISTRADOR')
        if user_group:
            instance.groups.add(user_group)

@receiver(pre_save,sender=Usuario)
def update_group(sender,instance,**kwargs):
    #Elimina sus grupos
    instance.groups.clear()
    match instance.tipo:
        case 'Técnico':
            user,_ = Group.objects.get_or_create(name='TECNICO')
        case 'Cliente' :
            user,_ = Group.objects.get_or_create(name='CLIENTE')
        case 'Administrador':
            user,_ =  Group.objects.get_or_create(name='ADMINISTRADOR')
    instance.groups.add(user)
   





