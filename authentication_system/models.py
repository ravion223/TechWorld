from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ACCESS_ROLES = [
        ('user', 'User'),
        ('admin', 'Administrator')
    ]

    email = models.EmailField(unique=True)
    access = models.CharField(max_length=31, choices=ACCESS_ROLES, default='user')

    def __str__(self) -> str:
        return f'User {self.email}, access - {self.access}'
    
    class Meta:
        ordering = ['email']
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class CustomUserProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profiles')

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Profile of user {self.user.username}"
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'