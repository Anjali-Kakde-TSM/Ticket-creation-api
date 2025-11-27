import requests
from typing import Any, Dict

from config.settings import JiraConfig
from auth.auth import get_auth_header

class JiraClient:
    """Jira Cloud REST API client."""

    def __init__(self, config: JiraConfig):
        self.cfg = config
        self.base_url = config.base_url.rstrip("/")
        self.headers = get_auth_header(config.email, config.api_token)

    def create_issue(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /rest/api/3/issue — Create a Jira issue."""
        url = f"{self.base_url}/rest/api/3/issue"
        response = requests.post(url, json=payload, headers=self.headers, timeout=30)
        response.raise_for_status()
        return response.json()
