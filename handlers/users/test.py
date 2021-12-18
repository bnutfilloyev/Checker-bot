import logging

from instaloader import Instaloader, Profile

# logging.Logger
L = Instaloader()
L.load_session_from_file('haminmoshotmi', '/Users/yoshlikmedia/Projects/Checker-bot/haminmoshotmi')
profile = Profile.from_username(L.context, 'yoshlik_media')
print("{} follows these profiles:".format(profile.username))

for followee in profile.get_followees():
    print(followee.username)