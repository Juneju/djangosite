from django.db import models
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=50,blank=True) #title
    category=models.CharField(max_length=50,blank=True) #label
    date_time=models.DateTimeField(auto_now_add=True) #time
    content=models.TextField(blank=True,null=True) #content
    
    #计算对象标准的url
    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])
        #return "/blog/%i/" %self.id
    
    def __str__(self):       #show the object by using its title
        return self.title
    
    class Meta:
        ordering=['-date_time']
        