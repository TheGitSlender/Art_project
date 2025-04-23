import streamlit as st
from utils.session import navigate_to
from utils.puzzles import render_puzzle

def show_fes():
    """Display the Fes region page."""
    st.title("Fes: Cultural Heart of Morocco")
    
    # Region background
    st.image("/api/placeholder/800/300", caption="The ancient medina of Fes")
    
    # Region description
    st.markdown("""
    Welcome to Fes, Morocco's cultural and spiritual center. Founded in the 9th century, 
    it hosts the world's oldest university and a UNESCO World Heritage medina that feels 
    like a living medieval city.
    
    Fes is renowned for:
    - The ancient Fes el-Bali medina with 9,000+ narrow streets
    - Traditional craftsmanship including pottery, leather, and metalwork
    - The historic Al-Qarawiyyin University and Library
    - The iconic blue gate (Bab Boujloud)
    - The famous tanneries where leather is processed using centuries-old methods
    """)
    
    # Display the current puzzle
    st.markdown("---")
    st.subheader("Challenges of Fes")
    render_puzzle("fes")
    
    # Navigation
    st.markdown("---")
    if st.button("Return to Map"):
        navigate_to("map")