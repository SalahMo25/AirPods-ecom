from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class discount_product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    prePrice = models.IntegerField()
    price = models.IntegerField()
    amount = models.IntegerField()
    desc = models.TextField(max_length=200)
    
    rating = models.DecimalField(default=0.0 , max_digits=3 , decimal_places=1) #avarage of rating
    all_ratings = models.IntegerField(default=0) #number of rating that happen from all users (when each user rates product , increse 1 )
    active = models.BooleanField(default=True)
    # user = models.ForeignKey(MyUser, blank=True , null=True, on_delete=models.SET_NULL)
    
    
    def __str__(self):
      return  self.name



class Rating(models.Model):
  product = models.ForeignKey(discount_product, on_delete=models.CASCADE , related_name='discount_ratings')
  value = models.IntegerField()
  
  def __str__(self):
      return  self.product.name