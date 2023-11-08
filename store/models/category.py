from django.db import models

class Category(models.Model):
    name= models.CharField(max_length=50, verbose_name="Kategoriya nomi")

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriya"
    
    def __str__(self):
        return self.name