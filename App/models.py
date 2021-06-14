from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    email = models.first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email=email)
        except:
            return False
    
    def isExists(self):
        if User.objects.filter(email=self.email):
            return True
        
        return False