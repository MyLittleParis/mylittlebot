import logging
from random import randint
import os

logger = logging.getLogger(f"random_lunch.{__name__}")

restaurants: list[dict[str, object]] = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Toriyoshi*\n :star::star::star::star: 136 reviews\n Restaurant Japonais: Sushi, Maki, brochettes,...\n\n 71 Rue Marguerite de Rochechouart, 75009 Paris"
        },
        "accessory": {
            "type": "image",
            "image_url": "https://lh3.googleusercontent.com/p/AF1QipP-dlCp7j3PcHN88noB-vPkonJDNJZoiqs4z8D5=s680-w680-h510",
            "alt_text": "alt text for image"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Tranché*\n :star::star::star::star: 136 reviews\n Boulangerie avec un néo-boulanger, rétro-passionné\n\n 62 Rue Marguerite de Rochechouart, 75009 Paris"
        },
        "accessory": {
            "type": "image",
            "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/ce/3e/0f/notre-boutique-tranche.jpg?w=900&h=500&s=1",
            "alt_text": "alt text for image"
        }
    },
]


def suggest_lunch(user_id: str) -> list[dict[str, object]]:
    random_index = randint(0, len(restaurants) - 1)

    logger.info(f"Restaurant #{random_index} has been randomly chosen.")

    return [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"Hey <@{user_id}>! Here is where you can eat:"},
        },
        {
            "type": "divider"
        },
        restaurants[random_index],
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
