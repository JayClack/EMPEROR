"""
Data classes to be used alongside the orbital mechanics functions and classes.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class omm:
    """
    Interface for Orbit Mean-Elements Messages, defined in CCSDS 502.0-B-3.

    The OMM data contains the sicth orbital elements required to propagate the orbit, in addition to identifying information on the object in question.

    object_name     -> spacecraft name for which mean element orbit state data is provided, string
    object_id       -> typically the international spacecraft designator as published in the UN Office of Outer Space Affairs designator index, string
                    -> recommended format = YYYY-NNNP{PP}, where YYYY is the year, NNN is the three digit serial number of launch, and P{PP} is used to identify the part brought into space by the launch.
    epoch           -> epoch of mean keplerian elements, datetime
    mean_motion     -> keplerian mean motion in revolutions per day, rev/day
    eccentricity    -> orbital eccentricity, dimensionless parameter describing the degree to which an orbit deviates from a perfect circle
    inclination     -> angle in degrees between the orbital plane and the reference plane, in this case the equatorial plane
    ra_asc_node     -> angle in degrees from a specified reference direction (origin of longitude) to the direction of the ascending node
                    -> for geocentric orbits the reference plane is the earths ecliptic plane
                    -> the ascending node is the node where the object passes north through the reference plane
                    -> the first point of aries is used as the origin of longitude for geocentric orbits
    arg_pericenter  -> angle in degrees between the ascending node and the its periapsis, measured in the direction of motion
    mean_anomaly    ->
    """
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