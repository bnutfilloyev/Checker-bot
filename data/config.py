from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
# CHANNELS = [-1001440890131, -1001183218634, -1001232814282]
#CHANNELS = [-1001579647791, -1001579647791]
CHANNELS = [-1001579647791, -1001551569027]

#INSTAGRAM_USERNAME = 'yoshlik_media'
INSTAGRAM_USERNAME = 'starbase.metaverse'
#SESSION_FILE = '/Users/yoshlikmedia/Projects/Checker-bot/haminmoshotmi'
SESSION_FILE = '/root/Workspace/Checker-bot/haminmoshotmi'
FACEBOOK_USERNAME = 'https://www.facebook.com/starbase.metaverse'
TWITTER_USERNAME = 'https://twitter.com/starbase_meta'
DISCORD_USERNAME = 'https://discord.gg/FUPKZChgcK'
YOUTUBE_USERNAME = 'https://www.youtube.com/channel/UCO6L41SD1e1_Di53vktEF3w'
