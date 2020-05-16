from django.db import models

class UserDetails(models.Model):
    first_name = models.CharField(("First Name"), max_length=200)
    last_name = models.CharField(("Last Name"), max_length=200)
    email = models.EmailField(("email "), max_length=254)
    mobile_num = models.IntegerField(("Phone Number"))
    level = models.IntegerField(("Level"))
    course = models.CharField(("Course"), max_length=50)
    date_posted = models.DateTimeField(("Date"), auto_now=True)
    

def __str__(self):
    return self.name
