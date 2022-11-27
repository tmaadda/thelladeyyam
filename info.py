import re
from os import environ
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 5540967 #int(environ['API_ID'],5540967)
API_HASH = 'eedf0196b0533f361b51b5b7082358e9'#(environ['API_HASH'],'eedf0196b0533f361b51b5b7082358e9')
BOT_TOKEN = '1877486792:AAGr4aoWtD_31Qh9GGnMnV2kUNYPqSxQSkY' #(environ['BOT_TOKEN'],'1877486792:AAGr4aoWtD_31Qh9GGnMnV2kUNYPqSxQSkY')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
PICS = (environ.get('PICS', 'https://telegra.ph/file/47a2366fee40ba6da37f6.jpg https://telegra.ph/file/72ca30a6a14428c36f776.jpg https://telegra.ph/file/5f091dc93a53e9a37a706.jpg https://telegra.ph/file/f5a76e1f71d5318e8035a.jpg https://telegra.ph/file/022720cc07cd137e84f59.jpg https://telegra.ph/file/06ecf5ce9045ad62f0479.jpg https://telegra.ph/file/4ac169e8871aa7be4d103.jpg https://telegra.ph/file/72d61ef5dff957ad2ff15.jpg https://telegra.ph/file/af126c7aae5e2c2a71b94.jpg https://telegra.ph/file/5425b244bc988f3534b22.jpg https://telegra.ph/file/1428e93eaca097e3046aa.jpg https://telegra.ph/file/620ebf7d4d2969837d538.jpg https://telegra.ph/file/1ea414cf5bb678ecf482b.jpg https://telegra.ph/file/8a4046ec3d2245357ecb9.jpg https://telegra.ph/file/e4d8973909f3f9beb0db5.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1086048529').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', " -1001201699325 -1001511163820 -1001435020763 -1001438293617").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1086048529 1242169194 18025669102 895955663 5388296061 2117090309 1665818466 1094503092 832312885 1902119538 1478286558 5348483742 1880167885 1848232918 909693392 837573929 1267798585 1225990769 1779025877 5213335284 5148112772').split()]

AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL','-1001367399738')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "-1001184830447 -1001367399738").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://erichdaniken:erichdaniken@cluster0.oh4dv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Dr_Strange_DataBase")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Doctor_Strange')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001112983591'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeleXMovies')

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a>/10 **\n\n Powered By @TeleXMovies**")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
