from dependency_injector import containers, providers

from src.config.env import environment
from src.config.database import Database, TenantDatabase

from src.infra.containers.tenants import TenantContainer
from src.infra.containers import UserContainer

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    db = providers.Singleton(
            Database, db_url=environment.get_item('DATABASE_URL') if not environment.get_item('TESTING', False) else environment.get_item('DATABASE_TEST_URL', 'sqlite:///')
        )
    tenant_db = providers.Singleton(TenantDatabase)

    tenant_container = providers.Container(TenantContainer, db=db, tenant_db=tenant_db)
    user_container = providers.Container(UserContainer, tenant_db=tenant_db)


def init_app() -> Container:
    return Container()
