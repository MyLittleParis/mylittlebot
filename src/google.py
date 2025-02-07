from pathlib import Path
import googlemaps
import os
import json


class GMaps:
    """Class to work with Gmaps"""
    gmaps: googlemaps.Client

    def __init__(self, client_key: str) -> None:
        self.gmaps = googlemaps.Client(key=client_key)

    def get_nearby_restaurants(self, lat: float, long: float) -> dict:
        return self._get_nearby_places(
            lat=lat,
            long=long,
            type="restaurant",
        )

    def _get_nearby_places(self, lat: float, long: float, type: str):
        places_from_file = self._get_places_from_cache()

        if places_from_file is not None:
            return places_from_file

        places_from_gmaps = self.gmaps.places_nearby(
            location=(lat, long),
            radius=1000,
            language="fr_FR",
            open_now=True,
            type=type,
        )

        self._save_places_in_file(places_from_gmaps)

        return places_from_gmaps

    def _get_places_from_cache(self) -> dict or None:
        places_file_path = os.path.join(os.getcwd(), "var", "cache", "places.json")

        file = Path(places_file_path)
        if not file.exists():
            return None

        with open(file=places_file_path, mode="r") as file:
            content = file.read()
            if not content or not content.strip():
                return None

            return json.loads(content)

    def _save_places_in_file(self, places: dict) -> dict or None:
        places_file_path = os.path.join(os.getcwd(), "var", "cache", "places.json")

        mode = "x+"
        file = Path(places_file_path)
        if file.exists():
           mode = "w+"

        with open(file=places_file_path, mode=mode, encoding="utf-8") as file:
            places_as_json = json.dumps(places)

            file.write(places_as_json)
