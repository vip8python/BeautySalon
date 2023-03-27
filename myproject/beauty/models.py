from django.db import models
from django.urls import reverse


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    register = models.DateField()
    email = models.CharField(max_length=50)
    registration_user = models.ForeignKey('Registration', on_delete=models.CASCADE, null=True, blank=True, related_name='user_list')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Specialist(models.Model):
    registration_id = models.ForeignKey('Registration', on_delete=models.CASCADE, null=True, blank=True, related_name='specialist_list')
    company = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=2000)
    calendar = models.DateTimeField()
    address = models.CharField(max_length=100)
    register = models.DateField()
    photo = models.ImageField(null=True)
    registration_specialist = models.ForeignKey('Registration', on_delete=models.CASCADE, null=True, blank=True, related_name='specialist')

    def __str__(self):
        return f'{self.company}'


class Services(models.Model):
    service_name = models.CharField(max_length=50)
    time = models.PositiveIntegerField(default=15)
    price = models.PositiveIntegerField(default=0)
    photo = models.ImageField(null=True, blank=True)
    specialist_services = models.ForeignKey('SpecialistServices', on_delete=models.CASCADE, null=True, blank=True, related_name='services')

    class Meta:
        verbose_name_plural = 'services'
    def __str__(self):
        return f'{self.service_name}'


class SpecialistServices(models.Model):
    specialist = models.ForeignKey('Specialist', on_delete=models.CASCADE)
    service = models.ForeignKey('Services', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'specialist services'



class Registration(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    specialist_specialist = models.ForeignKey('Specialist', on_delete=models.CASCADE)
