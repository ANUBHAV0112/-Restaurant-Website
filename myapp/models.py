from django.db import models



class booking(models.Model):
    name = models.CharField(max_length=30,primary_key=True)
    email = models.CharField(max_length=30)
    subject = models.TextField(default='')
    message = models.TextField()
    date = models.DateTimeField

    def __str__(self):
     return self.name

CHOICES=[('1','definetely'),
         ('2','maybe'),
         ('3','not Sure')]

rolech=[('1','individual',),
        ('2','couple'),('3','smallgroup'),('4','largegroup'),('5','preferno')]

pur=[('1','Date'),
         ('2','birthday'),
         ('3','anniversary'),
     ('4','party')]



class table(models.Model):
    name = models.CharField(max_length=30,primary_key=True) 
    date = models.CharField(max_length=230)
    email = models.EmailField(max_length = 254)
    time = models.CharField(max_length=12,default='')
    phone = models.CharField(max_length=10,default='')
    people = models.IntegerField(default='')
    message= models.TextField(max_length=300,null=True,blank=True)


    def __str__(self):
     return self.name

