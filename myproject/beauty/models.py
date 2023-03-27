from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    logo = models.ImageField(null=True)
    phone_number = models.CharField(max_length=20)
    register = models.DateField()
    email = models.CharField(max_length=50)
    registration = models.ForeignKey('Registration', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} '


class Specialist(models.Model):
    id = models.ForeignKey('Registration', on_delete=models.CASCADE, null=True, blank=True)
    id = models.ForeignKey('SpecialistServices', on_delete=models.CASCADE, null=True, blank=True)
    company = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=2000)
    calendar = models.DateTimeField()
    address = models.CharField(max_length=100)
    register = models.DateField()
    photo = models.ImageField(null=True)

    def __str__(self):
        return f'{self.company}'


class Services(models.Model):
    services = models.CharField(max_length=50)
    time = models.PositiveIntegerField(default=15)
    price = models.PositiveIntegerField(default=0)
    photo = models.ImageField(null=True, blank=True)
    specialist_services = models.ForeignKey('SpecialistServices', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.services}'


class SpeciaistServices(models.Model):
    specialist = models.IntegerField()
    services = models.IntegerField()


class Registration(models.Model):
    data = models.DateTimeField()
    user = models.IntegerField()
    specialist = models.IntegerField()
