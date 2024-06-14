import nsq
import logging
import graypy

# Configure logging
logger = logging.getLogger('consumer')
logger.setLevel(logging.DEBUG)
graylog_handler = graypy.GELFUDPHandler('localhost', 12201)
logger.addHandler(graylog_handler)

def message_handler(message):
    logger.info(f"Received message: {message.body.decode()}")
    return True

if __name__ == "__main__":
    reader = nsq.Reader(
        message_handler=message_handler,
        lookupd_http_addresses=['http://nsqlookupd:4161'],
        topic='todo_topic',
        channel='todo_channel'
    )
    nsq.run()
