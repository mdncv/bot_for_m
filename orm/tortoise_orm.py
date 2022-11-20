import sys
from typing import Final

from tortoise import Tortoise, ConfigurationError
from tortoise.exceptions import DBConnectionError

from configuration import EnvironmentKeys


class ORM:
    TORTOISE_ORM: Final = Tortoise()

    @classmethod
    async def orm_init(cls, *args, **kwargs) -> None:
        try:
            await cls.TORTOISE_ORM.init(config=EnvironmentKeys.DATA_BASE_SETTINGS)
            await cls.TORTOISE_ORM.generate_schemas()
            print('INFO:tortoise:Tortoise-ORM connected.', file=sys.stderr)
        except ConfigurationError:
            print('INFO:tortoise:The configuration of the ORM is invalid.', file=sys.stderr)
        except DBConnectionError:
            print('INFO:tortoise:Unable to connect to database.', file=sys.stderr)

    @classmethod
    async def orm_shutdown(cls, *args, **kwargs) -> None:
        await cls.TORTOISE_ORM.close_connections()
