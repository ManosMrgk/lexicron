import datetime
from fastapi import FastAPI
from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from zoneinfo import ZoneInfo
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.utils.wiktionary_wotd import get_word_of_the_day
from app.utils.email_utils import send_email, RECIPIENTS
from app.utils.email_template import build_wotd_newsletter_body

athens_tz = ZoneInfo("Europe/Athens")
scheduler = AsyncIOScheduler(timezone=athens_tz)

@asynccontextmanager
async def lifespan(app:FastAPI):
    scheduler.start()
    yield
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

@scheduler.scheduled_job('cron', hour=12, minute=00)
async def sent_daily_email():
    word = get_word_of_the_day()
    body = build_wotd_newsletter_body(word=word.word, uri=word.uri)
    send_email(to=RECIPIENTS, subject="Lexicron - Word of the day", body=body, html=True)
    print("Email sent")

@app.get("/health")
async def test():
    return "OK"
