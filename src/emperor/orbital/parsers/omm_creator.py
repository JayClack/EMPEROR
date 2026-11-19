from datetime import datetime
from ..models import OMM

def from_celestrak(omm_dict):
    return OMM(
        object_name=omm_dict["OBJECT_NAME"],
        object_id=omm_dict["OBJECT_ID"],
        epoch=datetime.fromisoformat(omm_dict["EPOCH"]),
        mean_motion=omm_dict["MEAN_MOTION"],
        eccentricity=omm_dict["ECCENTRICITY"],
        inclination=omm_dict["INCLINATION"],
        ra_asc_node=omm_dict["RA_OF_ASC_NODE"],
        arg_pericenter=omm_dict["ARG_OF_PERICENTER"],
        mean_anomaly=omm_dict["MEAN_ANOMALY"],
        ephemeris=omm_dict["EPHEMERIS_TYPE"],
        classification=omm_dict["CLASSIFICATION_TYPE"],
        norad_cat=omm_dict["NORAD_CAT_ID"],
        element_set_no=omm_dict["ELEMENT_SET_NO"],
        rev_at_epoch=omm_dict["REV_AT_EPOCH"],
        bstar=omm_dict["BSTAR"],
        mean_motion_dot=omm_dict["MEAN_MOTION_DOT"],
        mean_motion_ddot=omm_dict["MEAN_MOTION_DDOT"]
    )