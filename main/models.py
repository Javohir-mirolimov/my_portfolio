from django.db import models
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify




class Jobs(models.Model):
    name = models.CharField(max_length=25)

class Banner(models.Model):
    fullname = models.CharField(max_length=55)
    jobs = models.ManyToManyField(to='Jobs')

    def __str__(self):
        return self.fullname


class About(models.Model):
    website = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    city = models.CharField(max_length=25)
    age = models.IntegerField()
    degree = models.CharField(max_length=15)
    email = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    img = models.ImageField(upload_to="img_about/", null=True, blank=True)





class Facts(models.Model):
    happy_client = models.IntegerField()
    project = models.IntegerField()
    hour_of_support = models.IntegerField()
    award = models.IntegerField()


class Skill(models.Model):
    still = models.CharField(max_length=25)
    percentage = models.IntegerField(default=0)

class Javoxir(models.Model):
    item_name = models.CharField(max_length=25)
    date = models.CharField(max_length=100, null=True, blank=True)
    desription  = models.TextField()

    def __str__(self):
        return self.item_name


class Resumeroad(models.Model):
    title = models.CharField(max_length=255)
    items = models.ManyToManyField(to='Javoxir')





class Service(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=55)
    img = models.ImageField(upload_to="service_img/", null=True, blank=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    full_name = models.CharField(max_length=25)
    description = models.CharField(max_length=55)
    img = models.ImageField(upload_to="testimonial_img/")

    def __str__(self):
        return self.full_name



class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    subject = models.CharField(max_length=55)
    message = models.TextField(null=True, blank=True)


class Info(models.Model):
    address = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=13, null=True, blank=True, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    instagram = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    githup = models.CharField(max_length=255)

