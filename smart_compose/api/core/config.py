from starlette.config import Config
from starlette.datastructures import Secret

APP_VERSION = "0.0.1"
APP_NAME = "Sentiment prediction"
API_PREFIX = "/api"

config = Config(".env")

##############
# API CONFIG #
##############
API_KEY: Secret = config("API_KEY", cast=Secret)
IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)

################
# MODEL CONFIG #
################
DEFAULT_MODEL_PATH: str = config("DEFAULT_MODEL_PATH")
