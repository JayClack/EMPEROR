"""
Data classes to be used alongside the orbital mechanics functions and classes.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class omm:
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