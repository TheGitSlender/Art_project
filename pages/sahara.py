import streamlit as st
from utils.session import navigate_to
from utils.puzzles import render_puzzle

def show_sahara():
    """Display the Sahara region page."""
    st.title("Sahara: The Great Desert")
    
    # Region background
    st.image("assets/images/backgrounds/sahara_banner.jpg", caption="The majestic sand dunes of the Sahara")
    
    # Region description
    st.markdown("""
    Welcome to the Sahara Desert, the world's largest hot desert and a landscape of 
    otherworldly beauty. This vast sea of sand covers much of southern Morocco and offers 
    a glimpse into nomadic culture and ancient trade routes.
    
    The Moroccan Sahara features:
    - Towering sand dunes of Erg Chebbi and Erg Chigaga
    - Nomadic Berber and Tuareg traditions
    - Oasis settlements with palm groves
    - Traditional Gnawa music with African influences
    - Stunning night skies perfect for stargazing
    """)
    
    # Display the current puzzle
    st.markdown("---")
    st.subheader("Challenges of the Sahara")
    render_puzzle("sahara")
    
    # Navigation
    st.markdown("---")
    if st.button("Return to Map",key="sahara_map"):
        navigate_to("map")