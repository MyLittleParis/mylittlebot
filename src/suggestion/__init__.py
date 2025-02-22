import logging
from random import randint

from google import Maps

logger = logging.getLogger(f"random_lunch.{__name__}")

def suggest_lunch(lat: float, long: float, user_id: str) -> list[dict[str, object]]:
    """Returns a format slack payload with the suggested restaurant
    :param lat: float
    :param long: float
    :param user_id: str
    :return: list[dict[str, object]]
    """
    maps = Maps()
    nearby_restaurants_response = maps.get_nearby_restaurants(lat, long)
    nearby_restaurants = nearby_restaurants_response['results']

    random_index = randint(0, len(nearby_restaurants) - 1)

    suggest_restaurant = nearby_restaurants[random_index]
    formatted_restaurant = _format_suggested_restaurant(suggest_restaurant)

    logger.info(f"Restaurant #{random_index} has been randomly chosen.")

    return [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"Hey <@{user_id}>! Here is where you can eat:"},
        },
        {
            "type": "divider"
        },
        formatted_restaurant,
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "What do you think ?"
            },
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Let's go!",
                    },
                    "action_id": "yes_action"
                },
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Meh...no",
                    },
                    "action_id": "no_action"
                },
            ]
        }
    ]


def _format_suggested_restaurant(restaurant: dict[str, any]) -> dict[str, object]:
    name: str = restaurant["name"]
    address: str = restaurant["vicinity"]
    rating: float = restaurant["rating"]
    total_reviews: int = restaurant["user_ratings_total"]
    maps_link: str = f"https://www.google.com/search?q={name.replace(" ","+")}"

    review_stars = ":star:" * int(rating)

    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": f"*{name}*\n {review_stars} {total_reviews} reviews\n\n {address} \n\n<{maps_link}|Voir sur Google>"
        },
        # TODO: use image from googlemaps payload
        # "accessory": {
        #     "type": "image",
        #     "image_url": "https://lh3.googleusercontent.com/p/AF1QipP-dlCp7j3PcHN88noB-vPkonJDNJZoiqs4z8D5=s680-w680-h510",
        #     "alt_text": "alt text for image"
        # }
    }


__all__ = ["suggest_lunch"]
