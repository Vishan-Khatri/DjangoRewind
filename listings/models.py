from django.db import models
from django.contrib.auth.models import User

CITY_CHOICES = [
    ('Kathmandu','Kathmandu'), ('Lalitpur','Lalitpur'), ('Bhaktapur','Bhaktapur'),
    ('Pokhara','Pokhara'), ('Butwal','Butwal'), ('Chitwan','Chitwan'),
    ('Biratnagar','Biratnagar'), ('Birgunj','Birgunj'), ('Other','Other'),
]
ROOM_TYPES = [
    ('single','Single Room'), ('shared','Shared Room'),
    ('flat','Whole Flat'), ('pg','PG / Hostel'),
]
GENDER_PREF = [('M','Male Only'), ('F','Female Only'), ('A','Any Gender')]

class Listing(models.Model):
    owner          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    title          = models.CharField(max_length=150)
    description    = models.TextField(max_length=600)
    city           = models.CharField(max_length=50, choices=CITY_CHOICES)
    address        = models.CharField(max_length=250)
    rent           = models.PositiveIntegerField(help_text='Monthly rent in NPR')
    room_type      = models.CharField(max_length=10, choices=ROOM_TYPES)
    gender_pref    = models.CharField(max_length=1, choices=GENDER_PREF, default='A')
    available_from = models.DateField()
    furnished      = models.BooleanField(default=False)
    wifi           = models.BooleanField(default=False)
    water_included = models.BooleanField(default=False)
    latitude       = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, help_text='e.g. 27.7172')
    longitude      = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, help_text='e.g. 85.3240')
    photo          = models.ImageField(upload_to='listing_photos/', blank=True, null=True)
    is_active      = models.BooleanField(default=True)
    created_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} — {self.city} (NPR {self.rent})"

class ContactMessage(models.Model):
    listing    = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='messages')
    sender     = models.ForeignKey(User, on_delete=models.CASCADE)
    message    = models.TextField(max_length=500)
    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.sender.username} about '{self.listing.title}'"
