from dependency_injector.wiring import inject

from src.config.containers import Container

container = Container()

@inject
def get_tenant_connections() -> dict:
    list_tenant_service = container.tenant_container.list_tenant_service()
    tenants = list_tenant_service.list_tenants()
    binds = {}
    for tenant in tenants:
        conntection_string_uri = {
            'url': f'sqlite:///./core_{tenant.code}.db'
        }
        tenant_code = tenant.code
        binds[tenant_code] = conntection_string_uri
    return binds
