import os
from typing import Final


class EnvironmentKeys:

    TELEGRAM_BOT_TOKEN: Final = os.getenv('TOKEN', 'token_not_defined')

    DATA_BASE_SETTINGS: Final = dict(db_url='sqlite://bot_for_m_db.sqlite3',
                                     modules={'models': ['data_base.models.tortoise_orm_models']})

    REDIS_SETTINGS: Final = dict(host=os.getenv('REDIS_HOST', default='localhost'),
                                 port=os.getenv('REDIS_PORT', default=6379),
                                 db=os.getenv('REDIS_DB', default=0),
                                 prefix=os.getenv('REDIS_PREFIX', default='fsm'))
