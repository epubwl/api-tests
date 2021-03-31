import os


class BaseRoute:
    def __init__(self, hostname: str = os.environ["EPUBWL_HOSTNAME"]) -> None:
        self.hostname: str = hostname
        self.json_header: dict[str, str] = {"Content-Type": "application/json"}

    def get_authorization_header(self, token: str) -> dict[str, str]:
        return {"Authorization": f"Bearer {token}"}
