import pynder
import tokengetter
#see tokengetter.py for info on how to configure auth.info

fb_access_token = (tokengetter.get_access_token(tokengetter.auth_info[1], tokengetter.auth_info[2]))
#output for testing verification purposes only
session = pynder.Session(tokengetter.auth_info[0], fb_access_token)
print(tokengetter.auth_info[0])
print(tokengetter.auth_info[1])
print(tokengetter.auth_info[2])
print(fb_access_token)
#session.matches() # get users you have already been matched with
#session.update_location(latitude, longitude) # updates latitude and longitude for your profile
#session.profile  # your profile. If you update its attributes they will be updated on Tinder.
#users = session.nearby_users() # returns a iterable of users nearby