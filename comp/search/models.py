from django.db import models


# Create your models here.


class Condition(models.Model):
    condition=models.CharField(max_length=30)

    def __str__(self):
        return 'Condition: ' + str(self.condition)


class Region(models.Model):
    region = models.CharField(max_length=50)

    def __str__(self):
        return 'Region: '+ str(self.region)


class Vendor(models.Model):
    vendor = models.CharField(max_length=100)

    def __str__(self):
        return 'Vendors: '+str(self.vendor)


class Phone(models.Model):
    name = models.TextField(max_length=200)
    price = models.IntegerField()
    condition = models.ForeignKey(Condition, on_delete=models.DO_NOTHING)
    location = models.TextField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)
    image = models.CharField(max_length=200)
    link = models.CharField(max_length=500, primary_key=True)
    vendor= models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return 'Name: ' + str(self.name) + ', Price: '+  str(self.Price) + ', Condition: ' + str(self.condition) + ', Location: ' + str(self.Location) + ', Region: ' + str(self.region) + ', Image: ' + str(self.image) + ', Link ' + str(self.link)+ ', Vendor ' + str(self.vendor)  + ', Time: ' + str(self.time)  + ', Date: ' + str(self.date)

