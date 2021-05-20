from rest_framework import generics
from .serializers import ListingSerializer
from .models import Listing, BlockDay, HotelRoom
import datetime
from django.db.models import Q
from collections import defaultdict


# Create your views here.
class AvailableListAPI(generics.ListAPIView):
    """
    Class is used for filtering available Hotels/Apartment rooms.
    """
    serializer_class = ListingSerializer

    def get_queryset(self):
        """
        Function is used to get available Hotels/Apartment rooms.
        :return: listing queryset
        """
        max_price = self.request.query_params.get('max_price')
        check_in = self.request.query_params.get('check_in').split("-")
        check_out = self.request.query_params.get('check_out').split("-")
        check_in_date = datetime.date(*[int(i) for i in check_in])
        check_out_date = datetime.date(*[int(i) for i in check_out])
        block_days = BlockDay.objects.filter(
            Q(check_in__range=(check_in_date, check_out_date)) | Q(check_out__range=(check_in_date, check_out_date)))
        hotels_details_dict = defaultdict(list)
        blocked_hotels_list = []
        for block in block_days:
            room = block.hotel_room.room_number
            hotels_details_dict[block.hotel_room.hotel_room_type.hotel.title].append(room)
        for key, value in hotels_details_dict.items():
            total_rooms_counts = HotelRoom.objects.filter(hotel_room_type__hotel__title=key).count()
            booked_rooms_counts = len(value)
            vacant_rooms = total_rooms_counts - booked_rooms_counts
            if vacant_rooms == 0:
                blocked_hotels_list.append(key)
        available_listing = Listing.objects.filter(price__lte=max_price).exclude(title__in=blocked_hotels_list)
        return available_listing
