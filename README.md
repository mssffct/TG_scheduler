# Telegram Scheduler
#### App to create reminders to be received from Telegram bot

### Application capabilities

- Create and edit reminders, edit their importance level and inner text
- Reminders will be automatically send at the specified time by Telegram bot

### Installation
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
- After frontend application start up you will be able to use it in your browser on 'http://localhost:9000/'
- Register your account in register form
![image](https://github.com/mssffct/TG_scheduler/assets/49521506/f168dd0f-77bc-46a1-824e-6f3f39ab87c1)
- Send '/start' command to your bot, copy ID you received as an answer and save it in User settings form
![image](https://github.com/mssffct/TG_scheduler/assets/49521506/66bb04e6-aa91-4696-a442-6713bd0bcc66)
- Navigation: Use buttons on the leftside panel in order to move to Create Memo page, Edit memos page, User settings page or to logout
![image](https://github.com/mssffct/TG_scheduler/assets/49521506/2fbdb78a-baa1-4254-8803-42ff256799e5)
- Create your memo using Create Memo form
![image](https://github.com/mssffct/TG_scheduler/assets/49521506/a0435f5a-d54d-4046-bf38-c23dbecf6e02)
- Edit memo's data or delete them using Edit Memo page functionality
![image](https://github.com/mssffct/TG_scheduler/assets/49521506/225af975-efbb-43d1-8000-f014e3be1bc3)

## TODOS:
- fix frontend docker conteiner issues
- add tests to telegram_service microservices
- add tests to memos application in scheduler_backend DRF application


