from django.contrib import admin

from .models import Listing, HotelRoomType, HotelRoom, BookingInfo, BlockDay


class HotelRoomTypeInline(admin.StackedInline):
    model = HotelRoomType
    extra = 1
    show_change_link = True


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    inlines = [HotelRoomTypeInline]
    list_display = (
        'title',
        'listing_type',
        'country',
        'city',
    )
    list_filter = ('listing_type',)


class HotelRoomInline(admin.StackedInline):
    model = HotelRoom
    extra = 1


@admin.register(HotelRoomType)
class HotelRoomTypeAdmin(admin.ModelAdmin):
    inlines = [HotelRoomInline]
    list_display = ('hotel', 'title',)
    show_change_link = True


@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('room_number',)

#
# @admin.register(BookingInfo)
# class BookingInfoAdmin(admin.ModelAdmin):
#     pass


admin.site.register(BlockDay)
admin.site.register(BookingInfo)
