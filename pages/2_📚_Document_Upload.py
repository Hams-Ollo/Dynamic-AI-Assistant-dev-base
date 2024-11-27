"""
Document Upload page for the AI Assistant
"""
import streamlit as st
from pathlib import Path
import sys

# Add parent directory to path to import app modules
sys.path.append(str(Path(__file__).parent.parent))

def display_upload_interface():
    """Display the document upload interface."""
    st.title("📚 Document Upload")
    
    with st.container():
        st.markdown("""
        ## Upload Your Documents
        
        Enhance the AI Assistant's knowledge by uploading relevant documents. 
        The system will process and analyze these documents to provide more informed responses.
        """)
        
        # File uploader
        uploaded_files = st.file_uploader(
            "Choose files to upload",
            accept_multiple_files=True,
            type=['pdf', 'txt', 'docx', 'md']
        )
        
        if uploaded_files:
            for uploaded_file in uploaded_files:
                # Add file processing logic here
                st.success(f"✅ Successfully uploaded: {uploaded_file.name}")
                
    # Document Management Section
    with st.expander("📁 Manage Documents", expanded=False):
        st.markdown("""
        ### Current Documents
        
        View and manage your uploaded documents here.
        """)
        # Add document management logic here
        
    # Upload Guidelines
    with st.expander("ℹ️ Upload Guidelines", expanded=False):
        st.markdown("""
        ### Supported File Types
        - PDF documents (.pdf)
        - Text files (.txt)
        - Word documents (.docx)
        - Markdown files (.md)
        
        ### Best Practices
        1. Ensure documents are properly formatted
        2. Remove any sensitive information
        3. Use clear file names
        4. Keep files under 100MB
        """)

def main():
    """Main function for document upload page."""
    display_upload_interface()

if __name__ == "__main__":
    main()
