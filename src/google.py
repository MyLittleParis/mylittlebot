import googlemaps


class GMaps:
    """Class to work with Gmaps"""
    gmaps: googlemaps.Client

    def __init__(self, client_key: str) -> None:
        self.gmaps = googlemaps.Client(key=client_key)

    def get_nearby_restaurants(self, lat: int, long: int) -> None:
        return self.gmaps.places_nearby(
            location=(lat, long),
            radius=1000,
            language="fr_FR",
            open_now=True,
            type="restaurant",
        )

