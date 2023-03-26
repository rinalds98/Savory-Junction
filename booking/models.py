from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

TABLES_AVAILABLE = (
    (1, 'Table 1'),
    (2, 'Table 2'),
    (3, 'Table 3'),
    (4, 'Table 4'),
    (5, 'Table 5'),
    (6, 'Table 6'),
    (7, 'Table 7'),
    (8, 'Table 8'),
    (9, 'Table 9'),
    (10, 'Table 10'),
)

TIME_CHOICES = (
    ("5:00 PM", "5:00 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6:00 PM", "6:00 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7:00 PM", "7:00 PM"),
    ("7:30 PM", "7:30 PM"),
    ("8:00 PM", "8:00 PM"),
    ("8:30 PM", "8:30 PM"),
    ("9:00 PM", "9:00 PM"),
)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    table_number = models.IntegerField(choices=TABLES_AVAILABLE)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="5:00 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} - Table {self.table_number} - {self.day} - {self.time}"
