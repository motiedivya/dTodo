import pynsq
import logging

class NSQHandler:
    def __init__(self, address):
        self.writer = pynsq.Writer([address])
        self.logger = logging.getLogger("uvicorn")

    def publish(self, topic, message):
        try:
            self.writer.pub(topic, message.encode())
            self.logger.info(f"Published message to {topic}: {message}")
        except Exception as e:
            self.logger.error(f"Error publishing message to {topic}: {e}")

    def close(self):
        self.writer.close()
