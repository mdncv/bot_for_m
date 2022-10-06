import sys
from typing import Final

from aiogram import Dispatcher

from tortoise import Tortoise, ConfigurationError, run_async
from tortoise.exceptions import DBConnectionError

from configuration import EnvironmentKeys


class ORM:

    TORTOISE_ORM: Final = Tortoise()

    @classmethod
    async def orm_init(cls, dispatcher: Dispatcher = None) -> None:

        try:
            await cls.TORTOISE_ORM.init(**EnvironmentKeys.DATA_BASE_SETTINGS)
            await cls.TORTOISE_ORM.generate_schemas()
            print('INFO:tortoise:Tortoise-ORM connected.', file=sys.stderr)
        except ConfigurationError:
            print('INFO:tortoise:The configuration of the ORM is invalid.', file=sys.stderr)
        except DBConnectionError:
            print('INFO:tortoise:Unable to connect to database.', file=sys.stderr)

    @classmethod
    async def orm_shutdown(cls, dispatcher: Dispatcher = None) -> None:
        await cls.TORTOISE_ORM.close_connections()


async def main():
    pass


if __name__ == '__main__':

    run_async(main())
