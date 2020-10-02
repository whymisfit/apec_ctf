from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Team(models.Model):
    member = models.ForeignKey(User, verbose_name="Участник", on_delete=models.CASCADE)

    team_name = models.CharField(verbose_name="Название команды", max_length=128, unique=True)
    team_picture = models.ImageField(verbose_name="Изображение команды", )
    score = models.PositiveIntegerField(verbose_name="Количество очков", default=0)

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    def __str__(self):
        return "{} {}".format(self.team_name, self.score)


class Category(models.Model):
    category_name = models.CharField(verbose_name="Название категории", max_length=256, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category_name


class Task(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория задания", on_delete=models.CASCADE)
    solved = models.ManyToManyField(Team, verbose_name="Команда выполнившая задачу", null=True, blank=True)

    task_name = models.CharField(verbose_name="Название задания", max_length=512)
    task_description = models.TextField(verbose_name="Описание задания", max_length=1024)
    flag = models.CharField(verbose_name="Флаг", max_length=32, )
    points = models.PositiveIntegerField(verbose_name="Количество очков", default=0)

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"

    def __str__(self):
        return "{} {}".format(self.task_name, self.points)
