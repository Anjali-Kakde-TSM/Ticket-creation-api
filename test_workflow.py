#!/usr/bin/env python
"""Test script to verify the ticket creation workflow."""

from config.settings import JiraConfig
from jira_client.client import JiraClient
from jira_client.payloads import build_issue_payload

def test_workflow():
    print("=" * 60)
    print("JIRA Ticket Creation API - Workflow Test")
    print("=" * 60)
    
    # Load config
    cfg = JiraConfig.load()
    print("\n✓ Configuration loaded successfully")
    print(f"  - Base URL: {cfg.base_url}")
    print(f"  - Email: {cfg.email}")
    print(f"  - Project Key: {cfg.project_key}")
    
    # Validate configuration
    errors = []
    if not cfg.base_url:
        errors.append("JIRA_BASE_URL is missing")
    if not cfg.email:
        errors.append("JIRA_EMAIL is missing")
    if not cfg.api_token:
        errors.append("JIRA_API_TOKEN is missing")
    if not cfg.project_key:
        errors.append("JIRA_PROJECT_KEY is missing")
    
    if errors:
        print("\n✗ Configuration errors found:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    print("\n✓ All configuration values are set")
    
    # Create client
    try:
        jira = JiraClient(cfg)
        print("\n✓ JiraClient initialized successfully")
    except Exception as e:
        print(f"\n✗ Failed to initialize JiraClient: {e}")
        return False
    
    # Build payload
    try:
        payload = build_issue_payload("SCRUM", "Test Issue", "Test Description", "Task")
        print("\n✓ Issue payload generated successfully")
        print(f"  - Summary: {payload['fields']['summary']}")
        print(f"  - Issue Type: {payload['fields']['issuetype']}")
        print(f"  - Project: {payload['fields']['project']}")
        print(f"  - Description: ADF format (Atlassian Document Format)")
    except Exception as e:
        print(f"\n✗ Failed to generate payload: {e}")
        return False
    
    # Test API connection (optional - only if you want to test actual API call)
    print("\n" + "=" * 60)
    print("To create an actual issue, use the Streamlit app:")
    print("  streamlit run app.py")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    success = test_workflow()
    exit(0 if success else 1)
