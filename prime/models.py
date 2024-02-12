from django.db import models
import decimal

from validators.validator import zip_code_validator
# Create your models here.


class Address(models.Model):
    """Modelo da table de Endereço
    """
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    # Todo: Escrever validador de cep
    zip_code = models.CharField(max_length=10, validators=[zip_code_validator])
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = 'Addresses'

    def __str__(self) -> str:
        return f'{self.street} n°{self.number}'


class Store(models.Model):
    """Modelo da tabela de Store
    """
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="uploads", blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Store"
        verbose_name_plural = "Stores"
        ordering = ("-created_at",)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Modelo da tabela de Category
    """
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Item(models.Model):
    """Modelo da tabela de item
    """
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    description = models.CharField(max_length=100, blank=True, null=True)
    discount = models.IntegerField(default=0)
    categories = models.ManyToManyField(
        Category,
        related_name="items"
    )
    store = models.ForeignKey(
        Store,
        related_name="items",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name

    @property
    def promo(self):
        if self.discount > 0:
            return True
        return False

    @property
    def sell_price(self):
        return self.price - (decimal.Decimal(self.discount/100) * self.price)
