# Random Lunch Bot

## Stack

- Python 3
- Slack Bolt for Python

## Requirements

### Access Tokens
Generate every necessary token which requires the bot which can be found here [.env.dist](./.env.dist).

To generate them, you can follow the documentation [Access tokens](https://api.slack.com/authentication/token-types).

### Permissions

#### Socket mode

You need to enabled Socket Mode and accept:
- `Interactivity & Shortcuts`
- `Slash Commands`

### Slash Commands

Create a slash command named:

- `/random-lunch`

#### App-Level Tokens

Scopes:

- `connections:write`

#### Bot Token Scopes

Scopes:

- `chat:write`
- `chat:write:public`
- `commands`

### Environment variables

Create a `.env` file from the `.env.dist` and fill it before running the app.

## Development
### Installation

Create a virtualenv:

```sh
python -m venv .venv
```

Activate it:

```sh
source .venv/bin/activate
```

Install packages:

```sh
pip install -r requirements.txt
```

### Running the application

Run the command:

```sh
python src/app.py
```

## Interaction

You can use the command `/random-lunch` to get a restaurant suggestion.
