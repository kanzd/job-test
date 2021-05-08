from django.db import models

# Create your models here.


class Image(models.Model):
    id = models.AutoField
    images = models.ImageField(upload_to="images/")
    tag = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)



    