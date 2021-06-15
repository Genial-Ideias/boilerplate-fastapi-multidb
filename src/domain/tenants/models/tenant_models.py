from typing import Optional
from pydantic import BaseModel


class TenantModel(BaseModel):
    id: int
    name: str
    code: str
    domain: str
    is_active: Optional[bool]


class CreateTenantModel(BaseModel):
    name: str
    code: str
    domain: str
