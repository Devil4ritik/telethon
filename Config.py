import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "19081399"))
    API_HASH = os.environ.get("API_HASH", "5cb454dd819c930fb0a935ec87f68951")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5114978864:AAGzAVtifU4JflqV1cK8kcjstLqp8PGMFSk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzsBu7LAGNICUvUxKoXAgpUghIu7y9OnpGjw_T0CNfV6V6MKwOM7bPXKuD8jvCmjspDVODqXHgl8G2ICOuv6qiwDrNxZeMFF0pbfMjN4_D6UK-gqp5-P7B-vBcly6hASi_PYGgX5EA2HdhvtYitaeFR04yi9eey9SEnhYaEJSgXeMAv35nvNupUuC7fneSm3RoSAEHE6TVvnUZ1G0xTbHSJYLavy3nlMl6vz9T2hkNQbScT0Ot697_R8JTUAkpSy9ytpSLhwHiAWM5LW0xu0nC6jLZZHr9tt49LiPXpbd7fMeQ8uuML3X--xMvNkVsHNZ0HHPRhoPWUXnd4066-BuUAxOew=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "lucy_x_bot")
    SUPPORT = os.environ.get("SUPPORT", "do_din_ki_masti")
    CHANNEL = os.environ.get("CHANNEL", "noob_marcus")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/891c60e24ac1b0b7c464d.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/891c60e24ac1b0b7c464d.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5574209021"))
