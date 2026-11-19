from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class SatelliteRecord:
    # General identifiers
    norad_cat: str
    name: str

    # Configuration and tracking data
    last_update: datetime
    update_period: int # value in s
    expiry_period: int # value in s
    active: bool

    def dict(self):
        return asdict(self)