from django.db import models
from django.contrib.auth.models import User

class Feed( models.Model):
    pub_date= models.DateTimeField('date published') #최초 저장시에만 현재 날짜 적용
    text= models.TextField() 
    image = models.ImageField(upload_to='photos/%m/%d') # media/photos/월/날짜 폴더에 저장 
    author= models.ForeignKey(User, related_name='feeds', on_delete =models.CASCADE)
    
    def __str__(self):
        return "text:" + self.text
    def summary(self):
        return self.text[:100]