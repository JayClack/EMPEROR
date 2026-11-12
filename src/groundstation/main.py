from ..orbital import Celestrak

celestrakProvider = Celestrak()
iss_omm_test = ""

try:
    iss_omm_test = celestrakProvider.retrieve_omm(25544).dict()
except Exception as e:
    print(type(e).__name__)
    print(e)

print(iss_omm_test)