from dataclasses import dataclass

import datetime

@dataclass
class Sighting:
    id: int
    datetime: datetime
    city: str
    state: str
    country: str
    shape: str
    duration: int
    duration_hm: str
    comments: str
    date_posted: str
    latitude: float
    longitude: float

    def __hash__(self):
        return hash(self.id)
    def __str__(self):
        return f"ID:{self.id}"