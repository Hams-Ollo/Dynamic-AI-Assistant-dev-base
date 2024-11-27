"""
Home page for the Dynamic AI Assistant
"""
import streamlit as st
from pathlib import Path
import sys

# Add parent directory to path to import app modules
sys.path.append(str(Path(__file__).parent.parent))

def display_quick_guide():
    """Display the comprehensive guide."""
    st.title("🌟 Welcome to Multi-Agent AI Assistant")
    
    # Introduction with animated container
    with st.container():
        st.markdown("""
        ## 🎯 About This System
        
        Welcome to our advanced Multi-Agent AI Assistant! This intelligent system leverages multiple specialized AI agents 
        working together to provide comprehensive assistance for your tasks. Each agent has specific expertise and 
        collaborates seamlessly to deliver the best possible results.
        """)

    # Key Features in an expander
    with st.expander("✨ Key Features", expanded=True):
        st.markdown("""
        - 🤖 **Multi-Agent Architecture**
          - Specialized agents for different tasks
          - Collaborative problem-solving
          - Dynamic task delegation
        
        - 🧠 **Advanced Capabilities**
          - Context-aware conversations
          - Document analysis and understanding
          - Complex task breakdown and execution
          
        - 🔄 **Real-time Processing**
          - Live agent interaction visualization
          - Step-by-step reasoning display
          - Transparent decision-making process
        """)

    # Navigation Guide
    st.markdown("## 🗺️ Navigation Guide")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📱 Core Pages
        
        1. **🏠 Home (Current)**
           - System overview
           - Feature guides
           - Best practices
        
        2. **💬 Chat**
           - Multi-agent interactions
           - Context-aware discussions
           - Real-time processing
        """)
    
    with col2:
        st.markdown("""
        3. **📚 Document Upload**
           - File management
           - Knowledge base enhancement
           - Supported formats
        
        4. **📊 System Monitor**
           - Agent status tracking
           - Performance metrics
           - System health
        """)

def main():
    """Main function for home page."""
    display_quick_guide()

if __name__ == "__main__":
    main()
