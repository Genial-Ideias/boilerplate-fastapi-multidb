from typing import Iterator

from src.domain.tenants.models.tenant_models import TenantModel
from src.domain.tenants.repositories.tenant_repository import TenantRepository


class ListTenantService:

    def __init__(self, repository: TenantRepository):
        self._repository = repository

    def list_tenants(self) -> Iterator[TenantModel]:
        tenants = self._list_tenants()
        return tenants

    def _list_tenants(self) -> Iterator[TenantModel]:
        tenants = self._repository.list_tenants()
        return tenants
