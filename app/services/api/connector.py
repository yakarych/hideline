from app.services.api.outline_vpn.outline_vpn import OutlineVPN
from app.settings.config import load_config


def get_connection() -> OutlineVPN:
    return OutlineVPN(api_url=load_config().outline_api.api_url)
