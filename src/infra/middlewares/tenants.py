from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from dependency_injector.wiring import inject

import app

from src.config.containers import Container

container = Container()

class ConnectTenantDatabaseMiddleware(BaseHTTPMiddleware):

    @inject
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        label_code = request.headers['label_code']
        app.app.container.tenant_container.identify_connection_service().identify_connection(label_code)
        response = await call_next(request)
        return response
