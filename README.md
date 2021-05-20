# HotelBookingApp
## Summary:
Extend Django Project with Django REST Framework for a simple prebuild booking app that have:
- Apartment(single_unit) have booking information (price) directly connected to it.
- Hotels(multi-unit) have booking information (price) connected to each of their HotelRoomTypes.
- filtering through Listings and returning JSON response with available units based on search criterias.
- should handle large dataset of Listings.

1. We should be able to **block days** ( make reservations ) for each **Apartment** or **HotelRoom**.
    - **new** Model for blocked (reserved) days must be created

2. NEW **endpoint** where we will get available Apartments and Hotels based on:
	- **available days** (date range ex.: "from 2021-12-09 to 2021-12-12")
            - Hotel should have at least 1 Hotel Room available from any of the HotelRoomTypes
     - **max_price**:
		- Apartment price must be lower than max_price.
		- Hotel should have at least 1 Hotel Room without any blocked days in the range with price lower than max_price.
		-  hotels should display the price of the **cheapest HotelRoomType** with **available HotelRoom**.

##Django setup instructions.
Create a python virtual environment using below command.

**python3 -m venv virtual-env**

Activate the environment.

**source virtual-env/bin/activate**

Install dependencies.

**pip install -r requirements.txt**


**python manage.py migrate**

Run this command and your django app should be running on port 8000

**python manage.py runserver**

## Request example:

http://localhost:8000/api/v1/units/?max_price=100&check_in=2021-12-09&check_out=2021-12-12


