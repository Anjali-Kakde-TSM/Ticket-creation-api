from typing import Dict, Union


def _to_adf(text: str) -> Dict:
    """Convert plain text to Atlassian Document Format (ADF)."""
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {"type": "text", "text": text}
                ]
            }
        ]
    }


def build_issue_payload(
    project_key: str,
    summary: str,
    description: str,
    issue_type: Union[str, int] = "Task"
) -> Dict:
    """Generate minimal Jira Cloud issue payload that will NOT fail."""

    # Support both ID (int/str) or name
    if str(issue_type).isdigit():
        issue_type_block = {"id": str(issue_type)}
    else:
        issue_type_block = {"name": issue_type}

    return {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "description": _to_adf(description),  # FIXED to ADF
            "issuetype": issue_type_block
        }
    }
