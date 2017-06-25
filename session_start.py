import pynder
#see tokengetter.py for info on how to configure auth.info
import robobrowser #for obtaining facebook token
import re #for obtaining facebook token

auth_stream = open("auth.info")
auth_info = [line.rstrip() for line in auth_stream.readlines()]
auth_stream.close()
#facebook authentication info will be in auth.info as follows:
#line 1: facebook id number
#line 2: email
#line 3: password


MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"


def get_access_token(email, password):
    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")
    s.open(FB_AUTH)
    ##submit login form##
    f = s.get_form()
    f["pass"] = password
    f["email"] = email
    s.submit_form(f)
    ##click the 'ok' button on the dialog informing you that you have already authenticated with the Tinder app##
    f = s.get_form()
    s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
    ##get access token from the html response##
    access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]

    return access_token

fb_access_token = (get_access_token(auth_info[1], auth_info[2]))

session = pynder.Session(auth_info[0], fb_access_token)

#output for testing verification purposes only
print(auth_info[0])
print(auth_info[1])
print(auth_info[2])
print(fb_access_token)

#session.matches() # get users you have already been matched with
#session.update_location(latitude, longitude) # updates latitude and longitude for your profile
#session.profile  # your profile. If you update its attributes they will be updated on Tinder.
#users = session.nearby_users() # returns a iterable of users nearby