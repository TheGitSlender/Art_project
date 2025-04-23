import streamlit as st
from utils.session import navigate_to
from utils.puzzles import render_puzzle

def show_casablanca():
    """Display the Casablanca region page."""
    st.title("Casablanca: Modern Morocco")
    
    # Region background
    st.image("/api/placeholder/800/300", caption="The Hassan II Mosque and Casablanca skyline")
    
    # Region description
    st.markdown("""
    Welcome to Casablanca, Morocco's largest city and economic capital. This cosmopolitan 
    metropolis blends modern development with traditional Moroccan and Art Deco influences, 
    representing the forward-looking face of the country.
    
    Casablanca is notable for:
    - The stunning Hassan II Mosque with the world's tallest minaret
    - A thriving contemporary art scene
    - Distinctive Mauresque architecture combining Moorish styles with Art Deco
    - The historic Habous Quarter with its neo-traditional design
    - Modern entertainment and shopping districts
    """)
    
    # Display the current puzzle
    st.markdown("---")
    st.subheader("Challenges of Casablanca")
    render_puzzle("casablanca")
    
    # Final game completion check
    if all(st.session_state.progress[region]["completed"] for region in st.session_state.progress):
        st.markdown("---")
        st.balloons()
        st.success("🎉 Congratulations! You have completed the entire Morocco Art & Culture Escape Game! 🎉")
        st.markdown(f"""
        ## Your Final Score: {st.session_state.score}
        
        You have successfully explored all regions of Morocco and learned about its rich art and cultural heritage!
        
        Thank you for playing! We hope you've enjoyed this virtual journey through the beautiful country of Morocco.
        """)
    
    # Navigation
    st.markdown("---")
    if st.button("Return to Map"):
        navigate_to("map")