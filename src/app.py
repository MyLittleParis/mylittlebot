from pathlib import Path
from dotenv import dotenv_values
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


from google import GMaps
from suggestion import suggest_lunch

env = dotenv_values(Path.cwd().joinpath(".env"))

bot_token = env.get("SLACK_BOT_TOKEN")
signing_secret = env.get("SLACK_SIGNING_SECRET")
app_token = env.get("SLACK_APP_TOKEN")
verification_token = env.get("SLACK_VERIFICATION_TOKEN")

app = App(
    token=bot_token,
    signing_secret=signing_secret,
    verification_token=verification_token,
)


@app.command("/random-lunch")
def on_suggest_lunch(ack, respond, command) -> None:
    ack()
    respond(
        blocks=suggest_lunch(command["user_id"])
    )


@app.action("suggest_action")
def on_suggest_action(body, ack, say) -> None:
    ack()
    say(blocks=suggest_lunch(body['user']['id']))


@app.action("yes_action")
def on_suggest_action(body, ack, say) -> None:
    ack()
    say(f"<@{body['user']['id']}> accepts!")


@app.action("no_action")
def on_suggest_action(body, ack, say) -> None:
    ack()
    say(f"<@{body['user']['id']}> refuses!")


if __name__ == "__main__":
    mlp_location_lat = env.get("MLP_LOCATION_LAT") or "1"
    mlp_location_long = env.get("MLP_LOCATION_LONG") or "1"
    google_place_key = env.get("GOOGLE_PLACES_API_KEY") or "test"

    # gmaps = GMaps(client_key=google_place_key)
    # nearby_restaurants = gmaps.get_nearby_restaurants(float(mlp_location_lat), float(mlp_location_long))

    # print(nearby_restaurants)

    SocketModeHandler(app, app_token).start()

