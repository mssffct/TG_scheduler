# Telegram Scheduler
#### App to create reminders to be received from Telegram bot

### Application capabilities

- Create and edit reminders, edit their importance level and inner text
- Reminders will be automatically send at the specified time by Telegram bot

### Instalation
> You need to install node, git, Docker and docker-compose locally. Also you need to create your Telegram application (https://core.telegram.org/api/obtaining_api_id) and to register your Telegram bot (https://core.telegram.org/bots/tutorial)

- Clone repository to the folder you want
- Rename example.env file to .env in root directory. Change DJANGO_SECRET_KEY and POSTGRES_PASSWORD variables values to yours
- Rename example.env file to .env in 'telegram_service/receiver' and 'telegram_service/sender' directories and fill in the variable values with your data
- Run following commands in root directory:
```sh
docker compose build
docker compose up -d
```
- Your backend applications are running in docker compose now
- Move to 'scheduler_frontend/tg_scheduler' folder and run:
```sh
npm install
npm run dev
```
After frontend application start up you will be able to use it in your browser on 'http://localhost:9000/'
