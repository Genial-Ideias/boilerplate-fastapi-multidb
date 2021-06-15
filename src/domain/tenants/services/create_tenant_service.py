from src.domain.tenants.models.tenant_models import CreateTenantModel, TenantModel
from src.domain.tenants.repositories.tenant_repository import TenantRepository


class CreateTenantService:

    def __init__(self, repository: TenantRepository):
        self._repository = repository

    def create(self, create_tenant_model: CreateTenantModel) -> TenantModel:
        tenant = self._create(create_tenant_model)
        return tenant

    def _create(self, create_tenant_model: CreateTenantModel) -> TenantModel:
        tenant = self._repository.create_tenant(create_tenant_model)
        return tenant
