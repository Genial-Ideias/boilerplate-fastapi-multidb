from typing import Iterator

from src.infra.orm.entities.tenant import Tenant
from src.domain.tenants.models.tenant_models import CreateTenantModel, TenantModel


class TenantRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def create_tenant(self, create_tenant: CreateTenantModel) -> TenantModel:
        with self.session_factory() as session:

            tenant_entity = Tenant()
            tenant_entity.name = create_tenant.name
            tenant_entity.code = create_tenant.code
            tenant_entity.domain = create_tenant.domain

            session.add(tenant_entity)
            session.commit()
            session.refresh(tenant_entity)

            tenant_model = TenantModel(
                id=tenant_entity.id,
                name=tenant_entity.name,
                code=tenant_entity.code,
                domain=tenant_entity.domain,
                is_active=tenant_entity.is_active
            )

            return tenant_model

    def list_tenants(self) -> Iterator[TenantModel]:
        with self.session_factory() as session:
            return session.query(Tenant).all()

    def get_by_code(self, code: int) -> TenantModel:
        with self.session_factory() as session:
            return session.query(Tenant).filter(Tenant.code == code).first()

