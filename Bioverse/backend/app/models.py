from pydantic import BaseModel
from typing import List, Optional

class Dataset(BaseModel):
    id: str
    title: str
    domain: str
    description: str
    keywords: Optional[List[str]] = None
    data_url: Optional[str] = None
    data_type: Optional[str] = None
    release_date: Optional[str] = None

