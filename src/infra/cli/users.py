import typer
from dependency_injector.wiring import inject

from src.config.containers import Container
from src.config.database import TenantDatabase
from src.config.tenant_config import get_tenant_connections

from src.domain.users.models.user_models import CreateUserModel

app = typer.Typer()

container = Container()

@app.command()
@inject
def create(
    tenant: str,
    name: str = typer.Option(..., prompt=True),
    email: str = typer.Option(..., prompt=True),
    password: str = typer.Option(..., prompt=True),
    ):
    tenant_db: TenantDatabase = container.tenant_db()
    tenant_db.identify_connection(f'sqlite:///./core_{tenant}.db')
    user_repo = container.user_container.user_repository()
    create_user_model = CreateUserModel(
        name=name,
        email=email,
        password=password
    )
    user_repo.create_user(create_user_model)
    typer.echo('Usuário cirado com sucesso!')


@app.command()
@inject
def list_users(tenant: str):
    tenant_db: TenantDatabase = container.tenant_db()
    tenant_db.identify_connection(f'sqlite:///./core_{tenant}.db')
    user_repo = container.user_container.user_repository()

    users = user_repo.list_users()
    if users:
        for user in users:
            typer.echo(f'{user.id} - {user.name}')
    else:
        typer.echo('Nenhum usuário cadastrado')
