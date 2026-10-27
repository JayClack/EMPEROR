"""
Data classes to be used alongside the orbital mechanics functions and classes.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class OMM:
    """
    Orbit Mean-Elements Message (OMM) defined by CCSDS 502.0-B-3.

    Contains the orbital elements and metadata required to propagate
    an Earth-orbiting object's trajectory.
    """

    object_name: str
    object_id: str
    epoch: datetime

    # Keplerian elements
    mean_motion: float      # rev/day
    eccentricity: float
    inclination: float      # deg
    ra_asc_node: float      # deg
    arg_pericenter: float   # deg
    mean_anomaly: float     # deg

    # Metadata
    ephemeris: int
    classification: str
    norad_cat: int
    element_set_no: int
    rev_at_epoch: int

    # Perturbation terms
    bstar: float
    mean_motion_dot: float
    mean_motion_ddot: float

    @classmethod
    def from_dict(cls, dict) -> "OMM":
        return cls(
            object_name=dict["OBJECT_NAME"],
            object_id=dict["OBJECT_ID"],
            epoch=datetime.fromisoformat(dict["EPOCH"]),
            mean_motion=dict["MEAN_MOTION"],
            eccentricity=dict["ECCENTRICITY"],
            inclination=dict["INCLINATION"],
            ra_asc_node=dict["RA_OF_ASC_NODE"],
            arg_pericenter=dict["ARG_OF_PERICENTER"],
            mean_anomaly=dict["MEAN_ANOMALY"],
            ephemeris=dict["EPHEMERIS_TYPE"],
            classification=dict["CLASSIFICATION_TYPE"],
            norad_cat=dict["NORAD_CAT_ID"],
            element_set_no=dict["ELEMENT_SET_NO"],
            rev_at_epoch=dict["REV_AT_EPOCH"],
            bstar=dict["BSTAR"],
            mean_motion_dot=dict["MEAN_MOTION_DOT"],
            mean_motion_ddot=dict["MEAN_MOTION_DDOT"]
        )
