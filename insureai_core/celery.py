import os
from celery import Celery, signals

import os
from dotenv import load_dotenv

# look for .env in the project root
load_dotenv()  
# now os.environ["OPENAI_API_KEY"] will work

from openai import OpenAI
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "insureai_core.settings")
app = Celery("insureai")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@signals.worker_process_init.connect
def _seed_openai_env(**_):
    from django.conf import settings
    if getattr(settings, "OPENAI_API_KEY", None):
        os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
    if getattr(settings, "OPENAI_MODEL", None):
        os.environ["OPENAI_MODEL"] = settings.OPENAI_MODEL