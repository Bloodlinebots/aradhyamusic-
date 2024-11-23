#
# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, < https://github.com/THE-VIP-BOY-OP >.
#
# This file is part of < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
#

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

import config

from ..logging import LOGGER

TEMP_MONGODB = "mongodb+srv://sevexedits:5JyQbk44RuB2jQj6@cluster0.lezcv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning(
        "𝐍𝐎 𝐌𝐎𝐍𝐆𝐎 𝐃𝐁 𝐔𝐑𝐋 𝐅𝐎𝐔𝐍𝐃.. 𝐘𝐎𝐔𝐑 𝐁𝐎𝐓 𝐖𝐈𝐋𝐋 𝐖𝐎𝐑𝐊 𝐎𝐍 𝐀𝐑𝐀𝐃𝐇𝐘𝐀 𝐌𝐔𝐒𝐈𝐂 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄 "
    )
    temp_client = Client(
        "VIPMUSIC",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.VIPMUSIC
    pymongodb = _mongo_sync_.VIPMUSIC
