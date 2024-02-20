from pydantic import BaseModel


class ActivityRequest(BaseModel):
    participants: int
