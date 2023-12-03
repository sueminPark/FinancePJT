from django.db import models
from django.conf import settings


# Create your models here.
class Product(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    prdt_div = models.TextField(null=True)
    dcls_month = models.TextField(max_length=6, null=True)
    fin_co_non = models.TextField(null=True)
    kor_co_nm = models.TextField(null=True)
    fin_prdt_cd = models.TextField(null=True)
    fin_prdt_nm = models.TextField(null=True)
    mtrt_int = models.TextField(null=True)
    join_deny = models.TextField(null=True)
    join_member = models.TextField(null=True)
    max_limit = models.IntegerField(null=True)
    dcls_strt_day = models.TextField(null=True)
    dcls_end_day =  models.TextField(null=True)
    fin_co_subm_day = models.TextField(null=True)
    intr_rate_type = models.TextField(null=True)
    intr_rate_type_nm = models.TextField(null=True)
    save_trm = models.TextField(null=True)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)
    isWon = models.BooleanField(null=True)



class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


