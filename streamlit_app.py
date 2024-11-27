"""
Main entry point for Streamlit Cloud deployment
"""
import os
import sys
from pathlib import Path

import streamlit as st

# Set page configuration at the very beginning
st.set_page_config(
    page_title="Dynamic AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    sidebar_title="💬 AI Chat Assistant"
)

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Import the main frontend components
from frontend.Chat import main as chat_main

def init_session_state():
    """Initialize session state variables."""
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def main():
    """Main function to run the Streamlit application."""
    # Initialize session state
    init_session_state()

    # Run the main chat interface
    chat_main()

if __name__ == "__main__":
    main()
