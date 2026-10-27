from datetime import datetime
from ..models.omm import OMM

def from_celestrak(dict):
    return OMM(
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