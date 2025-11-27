from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass
class JiraConfig:
    """Configuration object for Jira Cloud connection."""
    base_url: str
    email: str
    api_token: str
    project_key: str

    @staticmethod
    def load() -> "JiraConfig":
        """Load Jira configuration from environment variables."""
        return JiraConfig(
            base_url=os.getenv("JIRA_BASE_URL", ""),
            email=os.getenv("JIRA_EMAIL", ""),
            api_token=os.getenv("JIRA_API_TOKEN", ""),
            project_key=os.getenv("JIRA_PROJECT_KEY", "DEMO"),
        )
