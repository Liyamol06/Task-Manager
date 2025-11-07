from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


#  Creating User models
class TaskUsers(models.Model):
    """
    Creating a model for Task Manger Users.

    Attributes:
        user_id(Foreign Key): User from the auth user model
        phone(CharField): Used RegexValidator for the validation
        photo(ImageField): uploads in media/profile_photos/
        created_on(DateTimeField): field for store the created date by using auto_now_add
    """

    phone_validator = RegexValidator(
        message= 'Please enter a valid phonenumber',
        regex = r'^(?:+91|0)?[6-9]\d{9}$',
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='task_user')
    phone = models.CharField(validators=[phone_validator], max_length=15, unique=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}".strip() or self.user.username
