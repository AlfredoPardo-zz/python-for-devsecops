DEBUG = True
BOT_URL = 'http://example-mattermost:8065/api/v4'
BOT_LOGIN = 'user@example.com'
BOT_PASSWORD = '$Str0ngPasswordHere'
BOT_TEAM = 'devsecbot'

PLUGINS = [
    'mmpy_bot.plugins',
    'custom_plugins',
    'custom_plugins.devsecbot'
]