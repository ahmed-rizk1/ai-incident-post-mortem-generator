from pydantic import BaseModel

class IncidentRequest(BaseModel):
    raw_logs: str

class IncidentResponse(BaseModel):
    content: str
