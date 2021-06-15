from fastapi import FastAPI

from src.infra.middlewares.tenants import ConnectTenantDatabaseMiddleware


def init_app(app: FastAPI) -> None:
    app.add_middleware(ConnectTenantDatabaseMiddleware)
