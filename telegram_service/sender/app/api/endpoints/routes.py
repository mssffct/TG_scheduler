from fastapi import APIRouter, status, UploadFile, File

from app import schemas
from app.services import message_send


router = APIRouter()


@router.post('/send_message', status_code=status.HTTP_200_OK)
async def send_plain_message(message: schemas.PlainMessageSend):
    await message_send(message, parse_mode='html')
    return
