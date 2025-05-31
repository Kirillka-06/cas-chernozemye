from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=200)
    translit = models.CharField(max_length=200)
    #image = models.ImageField('Картинка', upload_to='types/', blank=True)

    def __str__(self):
        return self.name
    

class Seed(models.Model):
    name = models.CharField(max_length=200)
    translit = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='seeds') 
    description = models.TextField()
    image = models.ImageField('Картинка', upload_to='seeds/', blank=True)

    def __str__(self):
        return self.type.name + ':' + self.name
