# Quick Start Guide - Creating Jira Tickets

## Getting Started in 2 Minutes

### Step 1: Verify Configuration
All credentials are already set in `.env`:
```env
JIRA_BASE_URL=https://anjalikakde48-1761725258057.atlassian.net
JIRA_EMAIL=anjalikakde48@gmail.com
JIRA_API_TOKEN=<your-token>
JIRA_PROJECT_KEY=SCRUM
```

### Step 2: Launch the Web App
```bash
# From the project root directory
streamlit run app.py
```

Your browser will open automatically to `http://localhost:8501`

### Step 3: Create a Ticket
1. **Summary**: Enter a brief title (required)
2. **Description**: Enter detailed description
3. **Issue Type**: Select from Task, Bug, or Story
4. Click **"Create Issue"**

### Step 4: Confirmation
You'll see:
- ✓ Success message with issue key (e.g., "SCRUM-123")
- Full API response JSON

---

## Code Examples

### Example 1: Create a Bug Report
```python
from config.settings import JiraConfig
from jira_client.client import JiraClient
from jira_client.payloads import build_issue_payload

cfg = JiraConfig.load()
jira = JiraClient(cfg)

payload = build_issue_payload(
    project_key="SCRUM",
    summary="Login button not working on mobile",
    description="Users cannot click the login button when viewing on iPhone",
    issue_type="Bug"
)

result = jira.create_issue(payload)
print(f"Bug reported: {result['key']}")
```

### Example 2: Create a Task
```python
payload = build_issue_payload(
    project_key="SCRUM",
    summary="Refactor authentication module",
    description="Improve code quality and add unit tests",
    issue_type="Task"
)

result = jira.create_issue(JiraConfig.load())
```

### Example 3: Create a Story
```python
payload = build_issue_payload(
    project_key="SCRUM",
    summary="Implement dark mode",
    description="Users should be able to toggle dark mode in settings",
    issue_type="Story"
)
```

---

## Supported Issue Types

| Type | Use Case |
|------|----------|
| **Task** | Work items, implementation tasks |
| **Bug** | Defects, issues found in testing |
| **Story** | User stories, features |

To add more types, modify the dropdown in `ui/form.py`:
```python
issue_type = st.selectbox("Issue Type", ["Task", "Bug", "Story", "Epic", "Subtask"])
```

---

## Error Handling

### Common Issues & Solutions

#### 1. "Failed: 401 Unauthorized"
- **Cause**: Invalid API token or email
- **Fix**: Verify credentials in `.env`

#### 2. "Failed: 400 Project key is required"
- **Cause**: Invalid JIRA_PROJECT_KEY
- **Fix**: Check your project key in Jira

#### 3. "Failed: 403 Issue type is not allowed"
- **Cause**: Issue type doesn't exist in project
- **Fix**: Use valid issue types for your project

#### 4. "Summary is required"
- **Cause**: Empty summary field
- **Fix**: Enter a summary in the form

---

## Advanced Usage

### Custom Issue Fields

To add custom fields (assignee, labels, priority), extend the payload:

```python
def build_issue_payload_advanced(
    project_key: str,
    summary: str,
    description: str,
    issue_type: str,
    assignee_id: str = None,
    labels: list = None,
    priority: str = "Medium"
) -> dict:
    """Generate Jira issue payload with additional fields."""
    
    payload = {
        "fields": {
            "project": {"key": project_key},
            "summary": summary,
            "description": _to_adf(description),
            "issuetype": {"name": issue_type},
            "priority": {"name": priority}
        }
    }
    
    if assignee_id:
        payload["fields"]["assignee"] = {"id": assignee_id}
    
    if labels:
        payload["fields"]["labels"] = labels
    
    return payload
```

### Batch Create Tickets

```python
from config.settings import JiraConfig
from jira_client.client import JiraClient
from jira_client.payloads import build_issue_payload

cfg = JiraConfig.load()
jira = JiraClient(cfg)

tickets = [
    ("Fix API timeout", "API calls timing out after 30s", "Bug"),
    ("Update docs", "Update README with new endpoints", "Task"),
    ("Add logging", "Implement structured logging", "Task"),
]

for summary, description, issue_type in tickets:
    payload = build_issue_payload(cfg.project_key, summary, description, issue_type)
    result = jira.create_issue(payload)
    print(f"Created: {result['key']}")
```

---

## Testing

### Test 1: Verify Configuration
```bash
python test_workflow.py
```

Expected output: All ✓ checks pass

### Test 2: Create Test Ticket via UI
1. Run: `streamlit run app.py`
2. Enter: Summary = "Test Ticket", Description = "Testing", Issue Type = "Task"
3. Verify: Issue created successfully with key

---

## Environment Variables

| Variable | Required | Example |
|----------|----------|---------|
| `JIRA_BASE_URL` | Yes | `https://your-org.atlassian.net` |
| `JIRA_EMAIL` | Yes | `user@example.com` |
| `JIRA_API_TOKEN` | Yes | `ATATT3xFfGF0...` |
| `JIRA_PROJECT_KEY` | Yes | `SCRUM` |

**Get API Token**: 
1. Go to https://id.atlassian.com/manage/api-tokens
2. Click "Create API token"
3. Copy the token and paste in `.env`

---

## Troubleshooting

### App won't start
```bash
# Verify dependencies
pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.13+
```

### Streamlit not responding
```bash
# Kill the app (Ctrl+C) and restart
streamlit run app.py --logger.level=debug
```

### API calls failing
```bash
# Test configuration
python test_workflow.py

# Check network connectivity
python -c "import requests; requests.get('https://www.google.com')"
```

---

## Files Overview

```
ticket-creation-api/
├── app.py                 # Streamlit entry point
├── config/
│   └── settings.py        # Load Jira credentials
├── auth/
│   └── auth.py            # Basic Auth header generation
├── jira_client/
│   ├── client.py          # Jira API client
│   └── payloads.py        # Payload builder
├── ui/
│   └── form.py            # Streamlit form UI
├── .env                   # Your credentials (KEEP SECRET!)
├── requirements.txt       # Python dependencies
└── test_workflow.py       # Test script
```

---

## FAQ

**Q: Is my API token secure?**
A: It's in `.env` locally only (not in git). For production, use a secrets manager.

**Q: Can I create issues in different projects?**
A: Yes, change `JIRA_PROJECT_KEY` in `.env` or modify the form.

**Q: What if the issue type doesn't exist?**
A: Check your Jira project settings for available issue types.

**Q: Can I assign issues automatically?**
A: Yes, extend the payload with `assignee` field (see Advanced section).

**Q: How do I add custom fields?**
A: Use the custom payload builder in Advanced section.

---

## Support Resources

- [Jira Cloud API Docs](https://developer.atlassian.com/cloud/jira/rest/v3/)
- [Atlassian Document Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/nodes/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

**Status**: ✓ Ready to use - No errors found
