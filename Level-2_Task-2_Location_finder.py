from geopy.geocoders import Nominatim
def location_of_the_user():
    geolocator = Nominatim(user_agent = "location_app")
    location = None
    while location is None:
        user_input = input("Please enter your location (city, country, etc.): ")
        try:
            location = geolocator.geocode(user_input)
        except Exception as e:
            print("Error occurred:", e)
            print("Please try again.")
    print("Your GPS coordinates:")
    print(f"Latitude: {location.latitude}")
    print(f"Longitude: {location.longitude}")
if __name__ == "__main__":
    location_of_the_user()
    
