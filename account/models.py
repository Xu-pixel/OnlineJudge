# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class AdminGroup(models.Model):
    pass


class UserManager(models.Manager):
    use_in_migrations = True

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})


class User(AbstractBaseUser):
    # 用户名
    username = models.CharField(max_length=30, unique=True)
    # 真实姓名
    real_name = models.CharField(max_length=30, blank=True, null=True)
    admin_group = models.ForeignKey(AdminGroup, null=True, on_delete=models.SET_NULL)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "user"