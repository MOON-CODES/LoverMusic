from LoverMusic.core.bot import LoverMusic
from LoverMusic.core.dir import dirr
from LoverMusic.core.userbot import Userbot
from LoverMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
dbb()
heroku()

app = LoverMusic()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
