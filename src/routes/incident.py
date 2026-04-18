from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from src.models.incident_models import IncidentRequest
from src.controllers.IncidentController import IncidentController

router = APIRouter(prefix="/api/incident", tags=["incident"])

@router.post("/generate")
def generate_incident(request: IncidentRequest):
    controller = IncidentController()
    try:
        def stream_generator():
            for chunk in controller.generate_post_mortem_stream(request.raw_logs):
                yield chunk
        return StreamingResponse(stream_generator(), media_type="text/plain")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
