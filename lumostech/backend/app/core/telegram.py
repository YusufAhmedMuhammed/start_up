import os
import requests
import logging
from typing import Optional
from datetime import datetime, timedelta
from app.core.config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self):
        self.token = settings.TELEGRAM_BOT_TOKEN
        self.chat_id = settings.TELEGRAM_CHAT_ID
        self.base_url = f"https://api.telegram.org/bot{self.token}"
        self.last_message_time = None
        self.message_queue = []
        self.max_retries = 3
        self.retry_delay = 1  # seconds

    def _can_send_message(self) -> bool:
        """
        Check if we can send a message based on rate limiting
        """
        if not self.last_message_time:
            return True
        
        time_since_last = datetime.now() - self.last_message_time
        return time_since_last >= timedelta(seconds=1)  # Rate limit: 1 message per second

    def _send_with_retry(self, text: str, retries: int = None) -> Optional[bool]:
        """
        Send a message with retry mechanism
        """
        if retries is None:
            retries = self.max_retries

        try:
            url = f"{self.base_url}/sendMessage"
            payload = {
                "chat_id": self.chat_id,
                "text": text,
                "parse_mode": "HTML"
            }
            response = requests.post(url, json=payload)
            
            if response.status_code == 200:
                self.last_message_time = datetime.now()
                return True
            
            if retries > 0:
                logger.warning(f"Failed to send message, retrying... ({retries} attempts left)")
                import time
                time.sleep(self.retry_delay)
                return self._send_with_retry(text, retries - 1)
            
            logger.error(f"Failed to send message after {self.max_retries} attempts")
            return False
            
        except Exception as e:
            logger.error(f"Error sending Telegram message: {str(e)}")
            if retries > 0:
                import time
                time.sleep(self.retry_delay)
                return self._send_with_retry(text, retries - 1)
            return False

    def send_message(self, text: str) -> Optional[bool]:
        """
        Send a message to the specified chat ID with rate limiting
        """
        try:
            if self._can_send_message():
                return self._send_with_retry(text)
            else:
                # Queue the message if rate limited
                self.message_queue.append(text)
                logger.info("Message queued due to rate limiting")
                return None
        except Exception as e:
            logger.error(f"Error in send_message: {str(e)}")
            return False

    def process_queue(self):
        """
        Process any queued messages
        """
        if self.message_queue and self._can_send_message():
            message = self.message_queue.pop(0)
            self._send_with_retry(message)

    def format_lead_message(self, lead_data: dict) -> str:
        """
        Format lead data into a readable Telegram message
        """
        try:
            return (
                "🚀 <b>New Lead Submitted!</b>\n\n"
                f"👤 <b>Name:</b> {lead_data['name']}\n"
                f"🏢 <b>Company:</b> {lead_data['company']}\n"
                f"📧 <b>Email:</b> {lead_data['email']}\n"
                f"📞 <b>Phone:</b> {lead_data['phone']}\n"
                f"💼 <b>Service Needed:</b> {lead_data['service_needed']}\n"
                f"📝 <b>Message:</b> {lead_data['message']}\n"
                f"⏰ <b>Submitted:</b> {lead_data['date_submitted']}"
            )
        except Exception as e:
            logger.error(f"Error formatting lead message: {str(e)}")
            return "Error formatting lead message"

# Create a singleton instance
telegram_bot = TelegramBot() 