from django.db import models
from datetime import date


class Listing(models.Model):
    HOTEL = 'hotel'
    APARTMENT = 'apartment'
    LISTING_TYPE_CHOICES = (
        ('hotel', 'Hotel'),
        ('apartment', 'Apartment'),
    )

    listing_type = models.CharField(
        max_length=16,
        choices=LISTING_TYPE_CHOICES,
        default=APARTMENT
    )
    title = models.CharField(max_length=255, )
    country = models.CharField(max_length=255, )
    city = models.CharField(max_length=255, )
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title


class HotelRoomType(models.Model):
    hotel = models.ForeignKey(
        Listing,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='hotel_room_types'
    )
    title = models.CharField(max_length=255, )

    def __str__(self):
        return f'{self.hotel} - {self.title}'


class HotelRoom(models.Model):
    hotel_room_type = models.ForeignKey(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='hotel_rooms'
    )
    room_number = models.CharField(max_length=255, )

    def __str__(self):
        return f'{self.hotel_room_type} - {self.room_number}'


class BookingInfo(models.Model):
    listing = models.OneToOneField(
        Listing,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_info'
    )
    hotel_room_type = models.OneToOneField(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='booking_info',
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        if self.listing:
            obj = self.listing
        else:
            obj = self.hotel_room_type

        return f'{obj} {self.price}'


class BlockDay(models.Model):
    booking_infos = models.ForeignKey(
        BookingInfo,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    hotel_room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE, null=True, blank=True)
    is_blocked = models.BooleanField(default=True)
    check_in = models.DateField(default=date.today)
    check_out = models.DateField(default=date.today)

    def __str__(self):
        return f'{self.check_in} - {self.check_out}'
