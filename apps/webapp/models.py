from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    team = models.ForeignKey('Team', verbose_name="Команда", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return "Profile: {}".format(self.user.username)


class Team(models.Model):
    team_name = models.CharField(verbose_name="Название команды", max_length=128, unique=True)
    team_picture = models.ImageField(verbose_name="Изображение команды", upload_to='team_pictures/')
    score = models.PositiveIntegerField(verbose_name="Количество очков", default=0)

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    def __str__(self):
        return "{}".format(self.team_name)


class Category(models.Model):
    category_name = models.CharField(verbose_name="Название категории", max_length=256, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category_name


class Task(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория задания", on_delete=models.CASCADE)
    solved = models.ManyToManyField(Team, verbose_name="Команда выполнившая задачу", default=None, blank=True)

    task_name = models.CharField(verbose_name="Название задания", max_length=512)
    task_description = models.TextField(verbose_name="Описание задания", max_length=1024)
    flag = models.CharField(verbose_name="Флаг", max_length=32, )
    points = models.PositiveIntegerField(verbose_name="Количество очков", default=0)
    attached_file = models.FileField(verbose_name="Прикрепленный файл", upload_to="attached_files/", null=True, blank=True)

    def get_short_file_name(self):
        return self.attached_file.name.replace("attached_files/", '')

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return "{} {}".format(self.task_name, self.points)
