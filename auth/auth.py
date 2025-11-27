import base64
from typing import Dict

def get_auth_header(email: str, api_token: str) -> Dict[str, str]:
    """Return Basic Auth header for Jira API."""
    raw = f"{email}:{api_token}".encode()
    encoded = base64.b64encode(raw).decode()

    return {
        "Authorization": f"Basic {encoded}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
