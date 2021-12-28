from django.db import models


class Customer_in(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag_in(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product_in(models.Model):
    class Meta:
        verbose_name = 'Продукт ИН'
        verbose_name_plural = 'Продукты ИН'

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag_in)

    def __str__(self):
        return self.name


class Order_in(models.Model):
    STATUS = (
        ('Обрабатывается', 'Обрабатывается'),
        ('В пути', 'В пути'),
        ('Доставлен', 'Доставлен')
    )
    customer = models.ForeignKey(Customer_in, on_delete=models.CASCADE,
                                 related_name='customer_in_order')
    product = models.ForeignKey(Product_in, on_delete=models.CASCADE,
                                related_name='product_in_order')
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200,
                              choices=STATUS, default='Обрабатывается')

    def __str__(self):
        return self.product.name
