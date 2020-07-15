from django.db import models


# Create your models here.
class Place(models.Model):
    userId = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    imageUrl = models.CharField(max_length=200)
    price = models.IntegerField()
    availableFrom = models.DateTimeField()
    availableTo = models.DateTimeField()

    create_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}".format(
            self.title)


class Booking(models.Model):
    userId = models.CharField(max_length=50)
    placeId = models.CharField(max_length=50)
    placeTitle = models.CharField(max_length=50)
    placeImage = models.CharField(max_length=200)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    guestNumber = models.IntegerField()
    bookedFrom = models.DateTimeField()
    bookedTo = models.DateTimeField()

    create_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}_{}".format(
            self.placeTitle, self.firstName, self.lastName)
