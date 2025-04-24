import streamlit as st

def initialize_session_state():
    """Initialize the session state variables if they don't exist."""
    if "page" not in st.session_state:
        st.session_state.page = "home"
    
    if "character" not in st.session_state:
        st.session_state.character = None
    
    if "unlocked_regions" not in st.session_state:
        st.session_state.unlocked_regions = ["marrakech"]
    
    if "completed_regions" not in st.session_state:
        st.session_state.completed_regions = []
    
    if "artifacts_collected" not in st.session_state:
        st.session_state.artifacts_collected = []
    
    if "progress" not in st.session_state:
        st.session_state.progress = {
            "marrakech": {"current_puzzle": 0, "total_puzzles": 3, "completed": False},
            "fes": {"current_puzzle": 0, "total_puzzles": 3, "completed": False},
            "chefchaouen": {"current_puzzle": 0, "total_puzzles": 3, "completed": False},
            "sahara": {"current_puzzle": 0, "total_puzzles": 3, "completed": False},
            "casablanca": {"current_puzzle": 0, "total_puzzles": 3, "completed": False}
        }
    
    if "hints_used" not in st.session_state:
        st.session_state.hints_used = 0
    
    if "score" not in st.session_state:
        st.session_state.score = 0

def navigate_to(page):
    """Change the current page in the session state."""
    st.session_state.page = page

def unlock_region(region):
    """Unlock a new region."""
    if region not in st.session_state.unlocked_regions:
        st.session_state.unlocked_regions.append(region)

def complete_region(region):
    """Mark a region as completed."""
    if region not in st.session_state.completed_regions:
        st.session_state.completed_regions.append(region)
    st.session_state.progress[region]["completed"] = True
    
    # Unlock next region based on completion order
    region_order = ["marrakech", "fes", "chefchaouen", "sahara", "casablanca"]
    current_index = region_order.index(region)
    if current_index < len(region_order) - 1:
        next_region = region_order[current_index + 1]
        unlock_region(next_region)

def add_artifact(artifact):
    """Add an artifact to the collected items."""
    if artifact not in st.session_state.artifacts_collected:
        st.session_state.artifacts_collected.append(artifact)
        st.session_state.score += 50

def advance_puzzle(region):
    """Advance to the next puzzle in the region."""
    current = st.session_state.progress[region]["current_puzzle"]
    total = st.session_state.progress[region]["total_puzzles"]
    
    if current < total:
        st.session_state.progress[region]["current_puzzle"] += 1
        st.session_state.score += 100
    
    # Check if all puzzles in the region are completed
    if st.session_state.progress[region]["current_puzzle"] >= total:
        complete_region(region)

def use_hint():
    """Use a hint, with a small score penalty."""
    st.session_state.hints_used += 1
    st.session_state.score = max(0, st.session_state.score - 25)  # Penalty for using hint

def reset_game():
    """Reset the game to its initial state."""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    initialize_session_state()