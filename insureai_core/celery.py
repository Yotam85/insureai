import os
from celery import Celery

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
