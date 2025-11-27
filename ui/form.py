import streamlit as st

from config.settings import JiraConfig
from jira_client.client import JiraClient
from jira_client.payloads import build_issue_payload

def render_issue_form():
    """Render Streamlit form for issue creation."""
    st.title("Create Jira Issue — Modular App")
    st.write("Use this form to create a Jira ticket using Jira REST API.")

    cfg = JiraConfig.load()

    with st.form("issue_form"):
        st.subheader("Issue Details")
        summary = st.text_input("Summary", "Example issue")
        description = st.text_area("Description", "Detailed description here...")
        issue_type = st.selectbox("Issue Type", ["Task", "Bug", "Story"])

        submitted = st.form_submit_button("Create Issue")

    if submitted:
        if not summary:
            st.error("Summary is required.")
            return

        jira = JiraClient(cfg)
        payload = build_issue_payload(cfg.project_key, summary, description, issue_type)

        with st.spinner("Creating issue..."):
            try:
                result = jira.create_issue(payload)
                st.success(f"Issue created: {result.get('key')}")
                st.json(result)
            except Exception as e:
                st.error(f"Failed: {e}")
