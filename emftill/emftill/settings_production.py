# Django settings for production use

from .settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = os.path.join(BASE_DIR, "../static")
