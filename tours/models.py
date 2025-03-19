from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone

# نموذج المستخدم المخصص
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_tour_guide = models.BooleanField(default=False)  

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # ✅ حل التعارض
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # ✅ حل التعارض
        blank=True
    )

    def __str__(self):
        return self.username
# نموذج الرحلات السياحية
class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='tours/', null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    guide_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255, null=True, blank=True)  # ✅ تم إضافته
    tour_guide = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)  # ✅ تم إضافته
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    guide = models.ForeignKey('TourGuide', on_delete=models.SET_NULL, null=True, blank=True)  # ✅ العلاقة مع المرشد السياحي


    def __str__(self):
        return self.title
class TourGuide(models.Model):  # ✅ تأكد أن الكلاس ليس abstract
    name = models.CharField(max_length=255)
    experience = models.TextField()

    def __str__(self):
        return self.name

# نموذج صور الجولة
class TourImage(models.Model):
    tour = models.ForeignKey(Tour, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tours/gallery/')

    def __str__(self):
        return f"{self.tour.title} - Image"

# نموذج الحجز
class Booking(models.Model):
    tour = models.ForeignKey(Tour, related_name='bookings', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    num_people = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} - {self.tour.title}"
