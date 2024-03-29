from django.contrib.auth.hashers import make_password
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image


class Client(models.Model):
    objects: models.Manager = models.Manager()
    username: str = models.CharField(max_length=50, default='')
    first_name: str = models.CharField(max_length=50)
    last_name: str = models.CharField(max_length=50)
    logo: models.ImageField = models.ImageField(upload_to='logo',
                                                null=True,
                                                blank=True)
    phone_number: str = models.CharField(max_length=20)
    register: models.DateField | None = models.DateField(null=True, blank=True)
    email: str = models.EmailField()
    password: str = models.CharField(max_length=50, default='')

    def save(self, *args, **kwargs):
        """
        Saves the Client instance with hashed password and username.
        """
        self.password = make_password(self.password)
        self.username = make_password(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        String representation of the Client instance.
        """
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        """
        Returns the absolute URL of the Client instance.
        """
        return reverse('client_detail', args=[str(self.id)])


class Specialist(models.Model):
    objects: models.Manager = models.Manager()
    company: str = models.CharField(max_length=50)
    first_name: str = models.CharField(max_length=50)
    last_name: str = models.CharField(max_length=50)
    descriptions: str = models.CharField(max_length=2000, null=True, blank=True)
    calendar: models.DateTimeField = models.DateTimeField(blank=True, null=True)
    address: str = models.CharField(max_length=100, null=True, blank=True)
    register: models.DateField = models.DateField(null=True, default=None)
    photo: models.ImageField = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        String representation of the Specialist instance.
        """
        return f'{self.company}'

    def get_absolute_url(self):
        """
        Returns the absolute URL of the Specialist instance.
        """
        return reverse('specialist_detail', args=[str(self.id)])


class SpecialistReview(models.Model):
    objects: models.Manager = models.Manager()
    specialist: Specialist = models.ForeignKey(Specialist, on_delete=models.SET_NULL, null=True, blank=True)
    reviewer: User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    review: str = models.TextField(max_length=2000)

    class Meta:
        verbose_name_plural = 'reviews'
        ordering = ['-date_created']

    def __str__(self):
        return self.review


class Services(models.Model):
    objects: models.Manager = models.Manager()
    service_name: str = models.CharField(max_length=50)
    time: models.PositiveIntegerField = models.PositiveIntegerField(default=15)
    price: models.PositiveIntegerField = models.PositiveIntegerField(default=0)
    photo: models.ImageField = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'services'

    def __str__(self):
        """
        String representation of the Services instance.
        """
        return f'{self.service_name}'


class SpecialistServices(models.Model):
    objects: models.Manager = models.Manager()
    specialist: Specialist = models.ForeignKey(Specialist, on_delete=models.SET_NULL, null=True, blank=True)
    service: Services = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'specialist services'

    def __str__(self):
        """
        String representation of the SpecialistServices instance.
        """
        return f'{self.specialist} - {self.service}'


class Registration(models.Model):
    objects: models.Manager = models.Manager()
    date: models.DateTimeField = models.DateTimeField()
    client: Client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    specialist: Specialist = models.ForeignKey(Specialist, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        """
        String representation of the Registration instance.
        """
        return f'{self.date} : {self.client} - {self.specialist}'


class Profile(models.Model):
    objects = models.Manager()
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    photo: models.ImageField = models.ImageField(default="profile_pics/default.png", upload_to="profile_pics")

    def __str__(self):
        """
        String representation of the Profile instance.
        """
        return f"{self.user.username} profile"

    def save(self, *args, **kwargs):
        """
        Saves the Profile instance and resizes the photo if needed.
        """
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 150 or img.width > 150:
            output_size = (150, 150)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    class Meta:
        verbose_name_plural = 'Profiles'
