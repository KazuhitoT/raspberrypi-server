from pydantic import BaseModel
import RPi.GPIO as GPIO
import time

from fastapi import FastAPI
import uvicorn

def vibration(id: int, duration: float):
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(id, GPIO.OUT)
        GPIO.output(id, True)
        time.sleep(duration)
    except Exception as e:
        print(e)
    finally:
        GPIO.output(id, False)


class VibrationParam(BaseModel):
    id: int
    duration: float


app = FastAPI()

@app.post("/vibration")
async def post_vibration(param: VibrationParam):
    vibration(param.id, param.duration)
    return '{"message": "OK"}'

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)