from dotenv import load_dotenv
import os
import dj_database_url

load_dotenv()


DATABASES = {
    'default': dj_database_url.config(
        default='DATABASE_URL',
        conn_max_age=600,
        conn_health_checks=True,
    )
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('DB_SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True