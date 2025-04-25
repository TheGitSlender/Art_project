import streamlit as st
from utils.session import navigate_to

def show_map():
    """Display the map of Morocco with unlocked regions."""
    st.title("Map of Morocco")
    
    # Character and score info
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Character: **{st.session_state.character.capitalize()}**")
    with col2:
        st.write(f"Score: **{st.session_state.score}** points")
    
    # Map image (placeholder)
    st.image("assets/images/backgrounds/morocco_map.png", caption="Map of Morocco", use_container_width=True)
    
    # Region selection
    st.subheader("Select a Region to Explore")
    
    # Display regions as cards in a grid
    col1, col2 = st.columns(2)
    
    # Marrakech
    with col1:
        st.markdown("<div class='region-card'>", unsafe_allow_html=True)
        st.subheader("Marrakech")
        st.image("assets/images/backgrounds/marrakech_thumbnail.jpg", caption="The Red City", use_container_width=True)
        
        # Check if completed or unlocked
        if "marrakech" in st.session_state.completed_regions:
            st.success("Completed!")
        
        if "marrakech" in st.session_state.unlocked_regions:
            if st.button("Explore Marrakech", key="explore_marrakech"):
                navigate_to("marrakech")
        else:
            st.warning("Region locked")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Fes
    with col2:
        st.markdown("<div class='region-card'>", unsafe_allow_html=True)
        st.subheader("Fes")
        st.image("assets/images/backgrounds/fes_thumbnail.jpg", caption="The Cultural Capital", use_container_width=True)
        
        # Check if completed or unlocked
        if "fes" in st.session_state.completed_regions:
            st.success("Completed!")
        
        if "fes" in st.session_state.unlocked_regions:
            if st.button("Explore Fes", key="explore_fes"):
                navigate_to("fes")
        else:
            st.warning("Region locked")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    # Chefchaouen
    with col1:
        st.markdown("<div class='region-card'>", unsafe_allow_html=True)
        st.subheader("Chefchaouen")
        st.image("assets/images/backgrounds/chefchaouen_thumbnail.jpg", caption="The Blue Pearl", use_container_width=True)
        
        # Check if completed or unlocked
        if "chefchaouen" in st.session_state.completed_regions:
            st.success("Completed!")
        
        if "chefchaouen" in st.session_state.unlocked_regions:
            if st.button("Explore Chefchaouen", key="explore_chefchaouen"):
                navigate_to("chefchaouen")
        else:
            st.warning("Region locked")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Sahara
    with col2:
        st.markdown("<div class='region-card'>", unsafe_allow_html=True)
        st.subheader("Sahara")
        st.image("assets/images/backgrounds/sahara_thumbnail.jpg", caption="The Desert", use_container_width=True)
        
        # Check if completed or unlocked
        if "sahara" in st.session_state.completed_regions:
            st.success("Completed!")
        
        if "sahara" in st.session_state.unlocked_regions:
            if st.button("Explore Sahara", key="explore_sahara"):
                navigate_to("sahara")
        else:
            st.warning("Region locked")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Casablanca (centered)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='region-card'>", unsafe_allow_html=True)
        st.subheader("Casablanca")
        st.image("assets/images/backgrounds/casablanca_thumbnail.jpg", caption="Modern Morocco", use_container_width=True)
        
        # Check if completed or unlocked
        if "casablanca" in st.session_state.completed_regions:
            st.success("Completed!")
        
        if "casablanca" in st.session_state.unlocked_regions:
            if st.button("Explore Casablanca", key="explore_casablanca"):
                navigate_to("casablanca")
        else:
            st.warning("Region locked")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Display artifacts collected
    if st.session_state.artifacts_collected:
        st.markdown("---")
        st.subheader("Your Collection")
        
        # Display artifacts in a grid
        num_artifacts = len(st.session_state.artifacts_collected)
        cols = st.columns(min(4, num_artifacts))
        pattern = r'([^/]+\.png)'

        for i, artifact in enumerate(st.session_state.artifacts_collected):
            with cols[i % min(4, num_artifacts)]:
               st.image(artifact, caption=artifact.split("/")[-1].split(".")[0], use_container_width=True)
    
    # Return to home button
    st.markdown("---")
    if st.button("Return to Main Menu", key="return_to_home"):
        navigate_to("home")