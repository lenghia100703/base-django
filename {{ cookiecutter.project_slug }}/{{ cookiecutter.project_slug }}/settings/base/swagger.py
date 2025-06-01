from .base import BACKEND_URL

SWAGGER_SETTINGS = {
    "DEFAULT_INFO": "parrot_edu_backend.settings.base.swagger.DEFAULT_INFO",
    "SECURITY_DEFINITIONS": {
        "JWT": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
    "USE_SESSION_AUTH": False,
    # 'LOGIN_URL': 'login',
    # 'LOGOUT_URL': 'logout',
    "VALIDATOR_URL": None,
}

if BACKEND_URL:
    SWAGGER_SETTINGS["DEFAULT_API_URL"] = BACKEND_URL
