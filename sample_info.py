# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 9301845
API_HASH = '563e9fd30b529442b705c7230f766b83'
BOT_TOKEN = '5003449601:AAHwaHLEmugQ1v0gzeNtAQzG75wMimScnqo'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [1952992043, 1713177274, 5299424797, 5348874903, 5421706941, 5510668711]
CHANNELS = [-10012345678, -100987654321, 'channelusername']
AUTH_USERS = []
AUTH_CHANNEL = '-1001860674667'

# MongoDB information
DATABASE_URI = "mongodb+srv://tmaadda:tmaadda@cluster0.8vqs89z.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = 'Tmamoviesbottt'
COLLECTION_NAME = 'Telegram_files'  # If you are using the same database, then use different collection name for each bot
LOG_CHANNEL = '-1001694472922'
PICS = 'https://telegra.ph/file/b6f42af4d20b757b46d73.jpg'
SUPPORT_CHAT = 'TMADISCUSS'
IMDB_TEMPLATE = "Hey {message.from_user.mention}, \n Here is the result for your {query}  \n <b>🏷 Title</b>: <a href={url}>{title}</a>  \n 📆 Year: <a href={url}/releaseinfo>{year}</a>  \n 🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.) \n ☀️ Languages : <code>{languages}</code> \n 📀 RunTime: {runtime} Minutes \n 📆 Release Info : {release_date} \n 🎛 Countries : <code>{countries}</code> \n Requested by : {message.from_user.mention}  \n Powered By @TMAAdda"
CUSTOM_FILE_CAPTION = '<b>{file_caption} \n Size :- <i>{file_size}</i> \n \n Join [TMAAdda](https://telegram.me/tmaadda)</b> '
SINGLE_BUTTON = "True"
UPSTREAM_REPO = "https://github.com/prajith2252/tmafilesbot"
