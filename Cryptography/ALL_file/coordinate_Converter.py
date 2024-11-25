from geopy.geocoders import Nominatim

# Function to find detailed location information from coordinates
def get_location_details(lat, lon):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.reverse((lat, lon), language="en")
    if location:
        # Extract relevant details from the address
        address = location.raw.get("address", {})
        country = address.get("country", "Unknown Country")
        state = address.get("state", "Unknown State")
        city = address.get("city", address.get("town", address.get("village", "Unknown City")))
        return f"{city}, {state}, {country}"
    else:
        return "Location not found"

# List of coordinates
coordinates = [
    (35.028309, 135.753082), 
    (46.469391, 30.740883), 
    (39.758949, -84.191605), 
    (41.015137, 28.979530), 
    (24.466667, 54.366669), 
    (3.140853, 101.693207),
    (9.005401, 38.763611), 
    (-3.989038, -79.203560), 
    (52.377956, 4.897070), 
    (41.085651, -73.858467), 
    (57.790001, -152.407227), 
    (31.205753, 29.924526)
]

# Loop through coordinates and find detailed location information
for coord in coordinates:
    details = get_location_details(coord[0], coord[1])
    print(f"Coordinates: {coord} -> Location: {details}")
