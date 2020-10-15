# DevSecBot for Mattermost

## Getting a Personal Access Token in Mattermost

* https://docs.mattermost.com/developer/personal-access-tokens.html

1. System Console > Integrations > Integration Management
    * Enable Personal Access Token
2. Account Settings -> Security -> Personal Access Tokens

## Notes:

* Please
    * ... replace `BOT_URL`, `BOT_LOGIN`, `BOT_PASSWORD` and `BOT_TEAM` with your mattermost configuration
    * ... export `POSTGRES_USERNAME`, `POSTGRES_PASSWORD`, `POSTGRES_HOST` and `POSTGRES_DATABASE` environment variables to point to the database with the Docker-Bench and Kube-Bench information.

## Running the bot

Run your bot by issuing the following command:

> $ MATTERMOST_BOT_SETTINGS_MODULE=mmpy_bot_settings mmpy_bot

(Mattermost should be already running)