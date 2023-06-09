from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from PIL import Image



class Client(models.Model):
    username = models.CharField(max_length=50, default='')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    register = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default='')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])


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
        return reverse('specialist_detail', args=[str(self.id)])


class SpecialistReview(models.Model):
    specialist = models.ForeignKey('Specialist', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    review = models.TextField(max_length=2000)

    class Meta:
        verbose_name_plural = 'reviews'
        ordering = ['-date_created']

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
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True, blank=True)
    specialist = models.ForeignKey('Specialist', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f'{self.date} : {self.client} - {self.specialist}'
#       return f'({self.date} {self.client.first_name})'

class Profilis(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} profilis"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.nuotrauka.path)
        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.nuotrauka.path)

    class Meta:
        verbose_name_plural = 'Profiles'

