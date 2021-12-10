# cremated-bot Self-hosted

## Setup:
- Install all requirements with `pip3 install -r requirements.txt`
- We recommend to use environment variables to configure your instance. To use it, set `ENV` to `True` and
then cofnigure `APP_URL`, `BOT_TOKEN`, `GITGRAM_SUPPORT`, `GIT_REPO_URL`, and `PROJECT_NAME` variables.
    - If you prefer the old way, edit your `config.py`, but DO NOT COMMIT!
- Run `python3 GitGram.py`

## Deploy on Heroku:
If you want to deploy this app on Heroku, there's a one-click setup for that. Click below, fill up the form and hit **Deploy App**.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/pokurt/GitGram)