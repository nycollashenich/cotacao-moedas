from django.db import models

class Base(models.Model):
    created_in = models.DateField('Criado em', auto_now_add=True)
    modificated = models.DateField('Modificado em', auto_now=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta():
        abstract = True

class Conversion(Base):
    from_currency = models.CharField(max_length=4)
    to_currency = models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    result = models.DecimalField(max_digits=10, decimal_places=2)
    conversion_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.amount} {self.from_currency} to {self.to_currency}"
    
    
