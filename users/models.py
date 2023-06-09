from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=256, verbose_name='Роль')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Skill(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    type = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Invite(models.Model):
    from_user = models.ForeignKey('CustomUser', on_delete=models.DO_NOTHING, verbose_name='Отправитель')
    message = models.TextField(verbose_name='Сообщение')
    accepted = models.BooleanField(null=True, verbose_name='Принято')

    def __str__(self):
        return self.from_user

    class Meta:
        verbose_name = 'Приглашение'
        verbose_name_plural = 'Приглашения'


class Achievement(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    type = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Тип')
    file = models.FileField(blank=True, verbose_name='Файл')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class Organization(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    address = models.TextField(verbose_name='Адрес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        user = self.model(username=username, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=256, unique=True, verbose_name='Логин')
    firstname = models.CharField(max_length=256, blank=True, verbose_name='Имя')
    lastname = models.CharField(max_length=256, blank=True, verbose_name='Фамилия')
    bio = models.TextField(blank=True, verbose_name='Био')
    birthday = models.DateField(blank=True, null=True, verbose_name='День рождения')
    role = models.ForeignKey('Role', blank=True, null=True, on_delete=models.DO_NOTHING, related_name='users', verbose_name='Роль')
    skills = models.ManyToManyField('Skill', blank=True, related_name='users', verbose_name='Навыки')
    experience = models.IntegerField(blank=True, default=0, verbose_name='Опыт')
    invites = models.ManyToManyField('Invite', blank=True, verbose_name='Приглашения')
    open = models.BooleanField(default=False, verbose_name='Открытый профиль')
    contacts = models.TextField(verbose_name='Контакты')
    achievements = models.ManyToManyField('Achievement', blank=True, verbose_name='Достижения')
    organization = models.ForeignKey('Organization', blank=True, null=True, on_delete=models.CASCADE, related_name='users', verbose_name='Организация')
    password = models.CharField(max_length=256, verbose_name='Пароль')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'