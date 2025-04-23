import streamlit as st
from utils.session import navigate_to, reset_game

def show_home():
    """Display the homepage of the application."""
    st.title("Morocco Art & Culture Escape Game")
    
    # Hero image
    st.image("assets/images/carrelage_asset.webp", caption="Journey through Morocco's rich art and cultural heritage")
    
    # Introduction text
    st.markdown("""
    ## Welcome to a Cultural Adventure!
    
    Embark on a virtual journey through Morocco's vibrant cities and landscapes. 
    Solve puzzles inspired by Moroccan art, history, and traditions to unlock new regions 
    and discover the rich cultural heritage of this beautiful North African country.
    
    In this escape game, you'll visit:
    
    - **Marrakech**: The Red City with its bustling souks and stunning palaces
    - **Fes**: The cultural capital known for traditional crafts and Islamic art
    - **Chefchaouen**: The Blue Pearl nestled in the Rif Mountains
    - **Sahara**: The majestic desert with nomadic traditions
    - **Casablanca**: The modern face of Morocco with contemporary art
    
    Collect artifacts, learn about Moroccan culture, and experience the magic of Morocco!
    """)
    
    # Character selection
    st.subheader("Choose Your Character")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("assets/images/carrelage_asset.webp", caption="The Traveler")
        traveler_selected = st.button("Select Traveler", key="select_traveler")
        if traveler_selected:
            st.session_state.character = "traveler"
    
    with col2:
        st.image("assets/images/carrelage_asset.webp", caption="The Artist")
        artist_selected = st.button("Select Artist", key="select_artist")
        if artist_selected:
            st.session_state.character = "artist"
    
    with col3:
        st.image("assets/images/carrelage_asset.webp", caption="The Historian")
        historian_selected = st.button("Select Historian", key="select_historian")
        if historian_selected:
            st.session_state.character = "historian"
    
    # Start game button - only enabled if character is selected
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.session_state.character:
            if st.button("Begin Your Moroccan Adventure", key="start_game"):
                navigate_to("map")
        else:
            st.warning("Please select a character to begin")
    
    # Reset game option
    with st.expander("Game Options"):
        if st.button("Reset Game"):
            reset_game()
            st.experimental_rerun()