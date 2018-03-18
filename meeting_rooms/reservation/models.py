from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=128)
    room_size = models.IntegerField()
    projector = models.BooleanField(default=None)
    #room_to_booking = models.ForeignKey("Booking", on_delete=models.CASCADE)

class Booking(models.Model):
    reserv_date = models.DateField(auto_now=False)
    room_id = models.ForeignKey(Room, related_name="room_id_room")
    comment = models.TextField()
    reservation = models.ManyToManyField(Room, through='BookingRooms')


class BookingRooms(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    room_resev_end = models.DateField()