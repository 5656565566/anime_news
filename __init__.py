from utils.permission import *
from .data_use import get_to_day_anime
from .get import get_data

from nonebot import on_command, on_regex
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot as Onebot, Event as Onebot_event
from nonebot.adapters.telegram import Bot as Telegram, Event as Telegram_event

from typing import Union
today_anime = on_regex(r'^(今日|今天|今)+.*(新番|番|动漫|番剧)+', permission=BAN, priority=5, block=True, rule=to_me())
get_anime = on_command('get anime', aliases={"更新番剧时间表"}, permission=pLEVEL4, priority=5, block=True)

scheduler = require("nonebot_plugin_apscheduler").scheduler

@today_anime.handle()
async def handle(
    bot: Union[Onebot, Telegram],
    event: Union[Onebot_event, Telegram_event]
    ):
    msg = get_to_day_anime()
    await today_anime.finish(msg)

@get_anime.handle()
async def handle(
    bot: Union[Onebot, Telegram],
    event: Union[Onebot_event, Telegram_event]
    ):
    msg = get_data()
    await get_anime.finish(msg)

@scheduler.scheduled_job("cron", hour="*/8")
async def news():
    get_data()
