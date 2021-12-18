from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
CHANNELS = [-1001440890131, -1001183218634]
INSTAGRAM_USERNAME = 'yoshlik_media'
# INSTAGRAM_USERNAME = 'abn.asia'
SESSION_FILE = '/Users/yoshlikmedia/Projects/Checker-bot/haminmoshotmi'
FACEBOOK_USERNAME = 'https://www.facebook.com/thanhsonnguyen'
TWITTER_USERNAME = 'https://twitter.com/steven_n_t'

