import streamlit as st
from utils.session import navigate_to
from utils.puzzles import render_puzzle

def show_marrakech():
    """Display the Marrakech region page."""
    st.title("Marrakech: The Red City")
    
    # Region background
    st.image("assets/images/backgrounds/marrakech_banner.jpg", caption="The vibrant medina of Marrakech")
    
    # Region description
    st.markdown("""
    Welcome to Marrakech, the "Red City" known for its historic medina, bustling souks, 
    and stunning palaces. This imperial city is a feast for the senses with its vibrant colors, 
    exotic scents, and the constant buzz of activity in Jemaa el-Fnaa square.
    
    Marrakech is famous for:
    - Intricate geometric patterns in architecture
    - Colorful zellige tilework
    - Traditional riads with interior gardens
    - The iconic Koutoubia Mosque
    - The historic Bahia Palace
    """)
    
    # Display the current puzzle
    st.markdown("---")
    st.subheader("Challenges of Marrakech")
    render_puzzle("marrakech")
    
    # Navigation
    st.markdown("---")
    if st.button("Return to Map"):
        navigate_to("map")