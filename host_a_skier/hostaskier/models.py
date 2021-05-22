from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    # max_length determines character length of title
    title = models.CharField(max_length=100)

    content = models.TextField()

    # setting default allows for time to be changed manually
    date_posted = models.DateTimeField(default=timezone.now)

    # using Django User model as datatype
    # on_delete meaning that if a user is deleted their posts are deleted
    auther = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
