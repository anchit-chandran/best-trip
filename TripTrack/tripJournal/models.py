from django.db import models

# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class TripReport(models.Model):

    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES)
    date_of_trip = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    entry_text = models.TextField()

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.author})"

    def truncate_entry(self)->str:
        """
        Fn to return a truncated version of `entry_text` property, trunacting with '...' after 50 chars.
        """
        return self.entry_text[:201] + '...'