import streamlit as st
from ui.form import render_issue_form

def main():
    st.set_page_config(page_title="Jira Create Issue", layout="centered")
    render_issue_form()

if __name__ == "__main__":
    main()
