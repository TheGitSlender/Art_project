import streamlit as st
from utils.session import initialize_session_state
from pages.home import show_home
from pages.map import show_map
from pages.marrakech import show_marrakech
from pages.fes import show_fes
from pages.chefchaouen import show_chefchaouen
from pages.sahara import show_sahara
from pages.casablanca import show_casablanca

# Set page config
st.set_page_config(
    page_title="Morocco Art & Culture Escape Game",
    page_icon="🇲🇦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #FCF5E5;
    }
    h1, h2, h3 {
        color: #B22222;
        font-family: 'Georgia', serif;
    }
    .stButton button {
        background-color: #D2691E;
        color: white;
        border-radius: 20px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .success-text {
        color: #006400;
        font-size: 18px;
        font-weight: bold;
    }
    .region-card {
        background-color: #FFFFFF;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Initialize session state
    initialize_session_state()
    
    # Navigation based on session state
    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "map":
        show_map()
    elif st.session_state.page == "marrakech":
        show_marrakech()
    elif st.session_state.page == "fes":
        show_fes()
    elif st.session_state.page == "chefchaouen":
        show_chefchaouen()
    elif st.session_state.page == "sahara":
        show_sahara()
    elif st.session_state.page == "casablanca":
        show_casablanca()

if __name__ == "__main__":
    main()