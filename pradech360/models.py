from django.db import models
from django.http import request

class For_partnership(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    c_code = models.IntegerField()
    phone = models.IntegerField()
    contry = models.CharField(max_length=50)
    sent_date = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=50)
    page_url = models.URLField(max_length=240)
    how_you_heared_about_us = models.CharField(max_length=50)
    Industry_type = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["-sent_date"]


class For_creatives(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    _prof_name = models.CharField(max_length=50)
    website_url = models.URLField(max_length=250)
    email = models.EmailField(max_length=50)
    country_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    _city = models.CharField(max_length=50)
    _page_url = models.URLField(max_length=250)
    _user_Type = models.CharField(max_length=50)
    _obj = models.CharField(max_length=350)
    _how_you_heared_about_us = models.CharField(max_length=50)
    campaign = models.CharField(max_length=1000)
    _industry_type = models.CharField(max_length=50)
    sent_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["-sent_date"]
   

class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_article = models.TextField()
    sent_date = models.DateField(auto_now_add=True)
    Blog_image = models.ImageField()

    def __str__(self):
        return self.blog_title
    
    class Meta:
        ordering = ["-sent_date"]