from django.db import models

class Post(models.Model):
    job_title = models.CharField(max_length=100)
    job_data = models.CharField(max_length=250)
    ex_date = models.DateField(blank=True)
    scope = models.FileField(upload_to='personal/uploads/',blank=True)

    def __str__(self):
        return self.job_title