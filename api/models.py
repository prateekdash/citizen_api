from django.db import models

# Create your models here.
class citizens(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    company_name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    email= models.EmailField(max_length=70, blank=False, unique=True)
    web = models.URLField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name