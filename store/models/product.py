from django.db import models
from .category import Category
class Products(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nomi")
    price= models.IntegerField(default=0, verbose_name="Narxi")
    category= models.ForeignKey(Category,on_delete=models.CASCADE,default=1,verbose_name="Kategoriya")
    description= models.CharField(max_length=250, default='', blank=True, null= True, verbose_name="Qo'shimcha ma'lumotlar")
    image= models.ImageField(upload_to='uploads/products/', verbose_name="Rasm")

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products();

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"