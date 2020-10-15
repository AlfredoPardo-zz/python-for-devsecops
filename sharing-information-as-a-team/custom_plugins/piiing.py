# -*- coding: utf-8 -*-

import re

from mmpy_bot.bot import respond_to


@respond_to('^piiing$', re.IGNORECASE)
def ping_reply(message):
    message.reply('pooong')


ping_reply.__doc__ = "Send poooong"
