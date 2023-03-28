from django.db import models
from django.urls import reverse


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    register = models.DateField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])


class Specialist(models.Model):
    company = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=2000)
    calendar = models.DateTimeField()
    address = models.CharField(max_length=100)
    register = models.DateField()
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.company}'

    def get_absolute_url(self):
        return reverse('specialist-detail', args=[str(self.id)])


class Services(models.Model):
    service_name = models.CharField(max_length=50)
    time = models.PositiveIntegerField(default=15)
    price = models.PositiveIntegerField(default=0)
    photo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'services'

    def __str__(self):
        return f'{self.service_name}'


class SpecialistServices(models.Model):
    specialist = models.ForeignKey('Specialist', on_delete=models.SET_NULL, null=True, blank=True)
    service = models.ForeignKey('Services', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'specialist services'

    def __str__(self):
        return f'{self.specialist} - {self.service}'


class Registration(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)
    specialist = models.ForeignKey('Specialist', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.date} : {self.user} - {self.specialist}'
#       return f'({self.date} {self.user.first_name})'
