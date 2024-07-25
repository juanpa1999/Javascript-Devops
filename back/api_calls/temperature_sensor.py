from fastapi import APIRouter, HTTPException, WebSocket,WebSocketDisconnect, Query
from managers.temperature_sensor import TemperatureSensor
from schemas.request.sensor_input_data import TemperatureRegistrationData
import asyncio
import logging

router = APIRouter(prefix="/temperature_sensor", tags=["temperature_sensor"],
                   responses={401: {"user": "Not authorized"}})

"""@router.get("/show_all_temperatures/", description="Allows users to get all cases")
async def get_all_cases(current_user: dict = Depends(AuthManager.get_current_user)):
    if current_user is None:
        raise HTTPException(status_code=403, detail="User Not Recognize")
    elif current_user["user_role"] in [UserRole.master, UserRole.admin, UserRole.operator]:
        temperatures = await TemperatureSensor.get_all_temperatures()
        return temperatures
    else:
        raise HTTPException(status_code=403, detail="Not authorized to view cases")"""


@router.get("/show_all_temperatures/", description="Allows users to get temperatures within a date range")
async def get_all_temperatures(start_date: str = Query(None, description="Start date in YYYY-MM-DD format"),
                                end_date: str = Query(None, description="End date in YYYY-MM-DD format")):
    try:
        temperatures = await TemperatureSensor.get_all_temperatures(start_date, end_date)
        return temperatures
    except HTTPException as e:
        raise e
    except:
        raise HTTPException(status_code=403, detail="Not authorized to view temperatures")


@router.post("/create_temperature/", description="Allows users to create a new temperature")
async def create_temperatures(temperature_data: TemperatureRegistrationData):
    try:
        result = await TemperatureSensor.create_temperature(temperature_data)
        return result
    except:
        raise HTTPException(status_code=403, detail="Unexpected error while uploading temperature sensor data -- Check if the sensor is registered and active.")


#websocket
@router.websocket("/ws/temperature")
async def websocket_temperature(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            temperatures = await TemperatureSensor.get_all_temperatures()
            json_data = [{"temperature": item.temperature, "creation_date": item.creation_date.isoformat()} for item in temperatures]
            await websocket.send_json(json_data)
            await asyncio.sleep(10)
    except WebSocketDisconnect:
        logging.info("Client disconnected")
    except Exception as e:
        logging.error(f"WebSocket error: {e}")
        await websocket.close(code=1000, reason=str(e))