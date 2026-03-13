from python.helpers.api import ApiHandler, Request, Response

from python.helpers.integrations import get_integrations_status


class IntegrationsStatus(ApiHandler):

    @classmethod
    def requires_auth(cls) -> bool:
        return False

    @classmethod
    def requires_csrf(cls) -> bool:
        return False

    @classmethod
    def get_methods(cls) -> list[str]:
        return ["GET", "POST"]

    async def process(self, input: dict, request: Request) -> dict | Response:
        status = get_integrations_status()
        return {"success": True, "integrations": status}
