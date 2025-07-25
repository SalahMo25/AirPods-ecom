from django.db import models

# Create your models here.
class all_products(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    prePrice = models.IntegerField()
    price = models.IntegerField()
    amount = models.IntegerField()
    desc = models.TextField(max_length=200)
    
    rating = models.DecimalField(default=0.0 , max_digits=3 , decimal_places=1) #avarage of rating
    all_ratings = models.IntegerField(default=0) #number of rating that happen from all users (when each user rates product , increse 1 )
    active = models.BooleanField(default=True)

    def __str__(self):
      return  self.name
    
class Rating(models.Model):
  product = models.ForeignKey(all_products, on_delete=models.CASCADE , related_name='all_products_ratings')
  value = models.IntegerField()
  
  def __str__(self):
      return  self.product.name