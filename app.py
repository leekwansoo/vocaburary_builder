import streamlit as st
import subprocess
import sys
import os
# Configure the app

st.set_page_config(

    page_title="Vocabulary Builder - App Selector",

    page_icon="🎓",

    layout="wide"

)

st.title("🎓 Vocabulary Builder - App Selector")

st.markdown("""
Welcome to the Vocabulary Builder Suite! This launcher helps you choose and start the right vocabulary learning app for your needs.

### 📚 Available Apps:
- **Basic Vocabulary Builder**: Simple interface, perfect for beginners
- **Advanced Vocabulary Builder**: Enhanced features with quizzes and phonetics
- **Custom Vocabulary Builder**: Full launcher with feature comparisons
""")

st.markdown("---")

apps = ["Basic Vocabulary Builder", "Advanced Vocabulary Builder", "Custom Vocabulary Builder"]

selected_app = st.sidebar.radio("Select App", apps)

# Add helpful information in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 App Information")

if selected_app == "Basic Vocabulary Builder":
    st.sidebar.markdown("""
    **Features:**
    - Clean, simple interface
    - Audio pronunciation
    - 3 difficulty levels
    - 8 categories with sample words
    - Perfect for beginners
    """)
elif selected_app == "Advanced Vocabulary Builder":
    st.sidebar.markdown("""
    **Features:**
    - Phonetic transcription (IPA)
    - Interactive quizzes
    - Progress tracking
    - Memory techniques
    - AI-powered learning
    """)
else:
    st.sidebar.markdown("""
    **Features:**
    - Complete feature overview
    - App comparison table
    - Learning path recommendations
    - Detailed descriptions
    """)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🚀 Quick Tips")
st.sidebar.markdown("""
- Each app runs on a different port
- You can run multiple apps simultaneously
- Check your browser for the launched apps
- Start with Basic if you're new to vocabulary building
""")

if selected_app == "Basic Vocabulary Builder":
    st.write("Launching Basic Vocabulary Builder...")
    if st.button("🚀 Launch Basic App"):
        try:
            # Launch the basic app in a new Streamlit process
            subprocess.Popen([
                sys.executable, "-m", "streamlit", "run", 
                os.path.join(os.path.dirname(__file__), "app_basic.py"),
                "--server.port", "8502"
            ])
            st.success("✅ Basic Vocabulary Builder launched! Check your browser at http://localhost:8502")
        except Exception as e:
            st.error(f"Failed to launch Basic App: {str(e)}")
    
elif selected_app == "Advanced Vocabulary Builder":
    st.write("Launching Advanced Vocabulary Builder...")
    
    # Show options for Advanced 1 or Advanced 2
    st.write("Choose your advanced version:")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎯 Launch Advanced 1"):
            try:
                subprocess.Popen([
                    sys.executable, "-m", "streamlit", "run", 
                    os.path.join(os.path.dirname(__file__), "app_advanced1.py"),
                    "--server.port", "8503"
                ])
                st.success("✅ Advanced 1 launched! Check your browser at http://localhost:8503")
            except Exception as e:
                st.error(f"Failed to launch Advanced 1: {str(e)}")
    
    with col2:
        if st.button("🚀 Launch Advanced 2"):
            try:
                subprocess.Popen([
                    sys.executable, "-m", "streamlit", "run", 
                    os.path.join(os.path.dirname(__file__), "app_advanced2.py"),
                    "--server.port", "8504"
                ])
                st.success("✅ Advanced 2 launched! Check your browser at http://localhost:8504")
            except Exception as e:
                st.error(f"Failed to launch Advanced 2: {str(e)}")
    
elif selected_app == "Custom Vocabulary Builder":
    st.write("Launching Custom Vocabulary Builder...")
    
    # Show launcher options
    if st.button("🎓 Open Full Launcher"):
        try:
            subprocess.Popen([
                sys.executable, "-m", "streamlit", "run", 
                os.path.join(os.path.dirname(__file__), "launcher.py"),
                "--server.port", "8505"
            ])
            st.success("✅ Full Launcher opened! Check your browser at http://localhost:8505")
        except Exception as e:
            st.error(f"Failed to launch Launcher: {str(e)}")
    
    st.info("💡 The Custom Vocabulary Builder provides access to all apps with detailed feature comparisons.")

# Add information about running apps
st.markdown("---")
st.markdown("### 🌐 App Access Information")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Available Ports:**
    - 🏠 Main Launcher: http://localhost:8501 (this app)
    - 📚 Basic App: http://localhost:8502
    - 🎯 Advanced 1: http://localhost:8503
    - 🚀 Advanced 2: http://localhost:8504
    - 🎓 Full Launcher: http://localhost:8505
    """)

with col2:
    st.markdown("""
    **Usage Notes:**
    - Each app runs independently
    - You can have multiple apps running
    - Close unused browser tabs to save resources
    - Refresh if an app doesn't load immediately
    """)

# Add a footer with helpful information
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-style: italic; padding: 20px;">
    <p>🎓 Vocabulary Builder Suite - Choose your learning path and start building your English vocabulary!</p>
    <p>Each app is designed for different learning levels and preferences. Start with Basic if you're unsure.</p>
</div>
""", unsafe_allow_html=True)
