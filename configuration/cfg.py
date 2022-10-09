import os
from typing import Final


class EnvironmentKeys:

    TELEGRAM_BOT_TOKEN: Final = os.getenv('TOKEN', 'token_not_defined')

    REDIS_SETTINGS: Final = dict(host=os.getenv('REDIS_HOST', default='localhost'),
                                 port=os.getenv('REDIS_PORT', default=6379),
                                 db=os.getenv('REDIS_DB', default=0),
                                 prefix=os.getenv('REDIS_PREFIX', default='fsm'))

    POSTGRES_HOST = os.getenv('POSTGRES_HOST', default='localhost')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT', default=5432)
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', default='1234')
    POSTGRES_USER = os.getenv('POSTGRES_USER', default='postgres')
    POSTGRES_DB = os.getenv('POSTGRES_DB', default='postgres')
    POSTGRES_URI = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'

    DATA_BASE_SETTINGS: Final = dict(connections={'default': POSTGRES_URI},
                                     apps={'models': {'models': ['orm.models.tortoise_orm_models'],
                                                      'default_connection': 'default'}
                                           })
