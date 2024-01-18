from django.db import models

class ProductType():
     pass

class Tv(models.Model):
    brand = models.CharField(max_length=10)
    model = models.CharField(max_length=30)
    screen_size = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    
    def __str__(self) -> str:
        return f"{(self.brand).upper()} {self.screen_size} inch TV "

    def sale_price(self):
        return '%.2f' %(float(self.price) * 0.85)
    

class Laptop(models.Model):
    brand = models.CharField(max_length=10)
    model = models.CharField(max_length=30)
    screen_size = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

        
    def __str__(self) -> str:
        return f"{(self.brand).upper()} {self.screen_size} inch Laptop "

    def sale_price(self):
        return '%.2f' %(float(self.price) * 0.85)
    

    
class Phone(models.Model):
        brand = models.CharField(max_length=10)
        model = models.CharField(max_length=30)
        price = models.DecimalField(max_digits=6, decimal_places=2, default=99.99)
        color = models.CharField(max_length=15, default='black')

            
        def __str__(self) -> str:
            return f"{(self.brand).upper()} {self.model} mobile phone "

        def sale_price(self):
            return '%.2f' %(float(self.price) * 0.85)
        

    
class Earbud(models.Model):
        brand = models.CharField(max_length=10)
        model = models.CharField(max_length=30)
        price = models.DecimalField(max_digits=6, decimal_places=2)
        with_lcd = models.BooleanField(default=False)

            
        def __str__(self) -> str:
            return f"{(self.brand).upper()} {self.model} earbuds "

        def sale_price(self):
            return '%.2f' %(float(self.price) * 0.85)
        
        