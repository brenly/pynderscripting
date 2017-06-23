import pynder
import tokengetter


#auth_info = open("auth.info").readlines()
#[l.strip('\n\r') for l in auth_info]

fb_access_token = (tokengetter.get_access_token(tokengetter.auth_info[1], tokengetter.auth_info[2]))
#print(fb_access_token)
session = pynder.Session(tokengetter.auth_info[0], fb_access_token)

#session.matches() # get users you have already been matched with
#session.update_location("33.2148", "97.1331") # updates latitude and longitude for your profile
#session.profile  # your profile. If you update its attributes they will be updated on Tinder.
#users = session.nearby_users() # returns a iterable of users nearby