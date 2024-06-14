from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import nsq
import graypy

app = FastAPI()

# Configure logging
logger = logging.getLogger('uvicorn')
logger.setLevel(logging.DEBUG)
graylog_handler = graypy.GELFUDPHandler('localhost', 12201)
logger.addHandler(graylog_handler)

todos = []

class TodoItem(BaseModel):
    item: str

class NSQHandler:
    def __init__(self, address):
        self.writer = nsq.Writer([address])
        self.logger = logging.getLogger("uvicorn")

    def publish(self, topic, message):
        try:
            self.writer.pub(topic, message.encode())
            self.logger.info(f"Published message to {topic}: {message}")
        except Exception as e:
            self.logger.error(f"Error publishing message to {topic}: {e}")

nsq_handler = NSQHandler("127.0.0.1:4250")

@app.post("/todo/")
async def create_todo_item(todo: TodoItem):
    try:
        todos.append(todo.item)
        nsq_handler.publish('todo_topic', todo.item)
        return {"message": "Todo item added"}
    except Exception as e:
        logger.error(f"Error creating todo item: {e}")
        return {"error": "Error creating todo item"}

@app.get("/todo/")
async def read_todo_items():
    try:
        return todos
    except Exception as e:
        logger.error(f"Error reading todo items: {e}")
        return {"error": "Error reading todo items"}

@app.delete("/todo/{index}")
async def delete_todo_item(index: int):
    try:
        removed_item = todos.pop(index)
        logger.info(f"Todo item deleted: {removed_item}")
        return {"message": "Todo item deleted"}
    except IndexError:
        logger.error(f"Failed to delete todo item at index: {index}")
        raise HTTPException(status_code=404, detail="Todo item not found")