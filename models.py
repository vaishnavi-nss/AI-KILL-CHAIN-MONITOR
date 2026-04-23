from pydantic import BaseModel

class Target(BaseModel):
    target: str   # IP or domain
