import streamlit as st
from utils.session import navigate_to
from utils.puzzles import render_puzzle

def show_chefchaouen():
    """Display the Chefchaouen region page."""
    st.title("Chefchaouen: The Blue Pearl")
    
    # Region background
    st.image("assets/images/backgrounds/chefchaouen_banner.jpg", caption="The blue streets of Chefchaouen")
    
    # Region description
    st.markdown("""
    Welcome to Chefchaouen, the ethereal "Blue Pearl" nestled in the Rif Mountains. 
    Founded in 1471, this town is famous for its striking blue-washed buildings and 
    relaxed atmosphere.
    
    Chefchaouen is known for:
    - The mesmerizing blue-painted houses and streets
    - Stunning mountain scenery and hiking opportunities
    - Rich Berber culture and traditions
    - Distinctive handicrafts including woven textiles
    - A fusion of Andalusian and Moroccan architectural styles
    """)
    
    # Display the current puzzle
    st.markdown("---")
    st.subheader("Challenges of Chefchaouen")
    render_puzzle("chefchaouen")
    
    # Navigation
    st.markdown("---")
    if st.button("Return to Map"):
        navigate_to("map")
