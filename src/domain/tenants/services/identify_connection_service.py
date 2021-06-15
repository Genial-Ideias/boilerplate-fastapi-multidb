from src.config.database import TenantDatabase

from src.shared.exceptions import HttpException

from src.domain.tenants.repositories.tenant_repository import TenantRepository


class IdentifyConnectionService:

    def __init__(self, repository: TenantRepository, tenant_db: TenantDatabase):
        self._repository = repository
        self._tenant_db = tenant_db

    def identify_connection(self, account_code: str) -> None:
        tenant = self._identify_connection(account_code)
        return tenant

    def _identify_connection(self, account_code: str) -> None:
        tenant = self._repository.get_by_code(account_code)

        if not tenant:
            raise HttpException(status_code=404, detail='Locatário não encontrado')

        self._tenant_db.identify_connection(f'sqlite:///./core_{tenant.code}.db')

