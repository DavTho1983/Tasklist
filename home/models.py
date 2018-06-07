from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        if len(self.description) < 30:
            return self.description

        return self.description[:30] + "..."

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
