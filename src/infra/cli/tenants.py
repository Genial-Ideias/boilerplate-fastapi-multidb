import typer
from dependency_injector.wiring import inject

from src.config.containers import Container

from src.domain.tenants.models.tenant_models import CreateTenantModel


app = typer.Typer()

container = Container()


@app.command()
@inject
def create(
    name: str = typer.Option(..., prompt=True),
    code: str = typer.Option(..., prompt=True),
    domain: str = typer.Option(..., prompt=True),
):
    create_tenant_service = container.tenant_container.create_tenant_service()
    create_tenant_model = CreateTenantModel(
        name=name,
        code=code,
        domain=domain
    )
    create_tenant_service.create(create_tenant_model)

    typer.echo('Tenant criado com sucesso!')


@app.command()
@inject
def list_tenants():
    list_tenant_service = container.tenant_container.list_tenant_service()
    tenants = list_tenant_service.list_tenants()
    if tenants:
        for tenant in tenants:
            typer.echo(f'{tenant.code} - {tenant.name}')
    else:
        typer.echo('Nenhum tentant cadastrado')
