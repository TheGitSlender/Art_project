import streamlit as st
import random
import numpy as np
import json
import os
from utils.session import advance_puzzle, add_artifact, use_hint

def load_puzzle_data(region, puzzle_number):
    """
    Simulated function to load puzzle data.
    In a real implementation, this would load from JSON files in the assets folder.
    """
    # Sample puzzle data - in production, load from JSON files
    puzzles = {
        "marrakech": [
            {
                "title": "The Colors of Marrakech",
                "description": "Match the traditional colors with their symbolic meanings in Moroccan culture.",
                "type": "matching",
                "options": {
                    "Red": "Strength and courage",
                    "Green": "Peace and wisdom",
                    "Blue": "Spirituality and protection",
                    "Yellow": "Happiness and prosperity"
                },
                "clue": "Think of how each color would guide emotions or rituals in Moroccan daily life.",
                "artifact": "Traditional Moroccan box"
            },
            {
                "title": "The Geometric Patterns",
                "description": "Arrange the tile patterns to complete the traditional Zellige mosaic.",
                "type": "pattern",
                "solution": [1, 3, 4, 2],
                "clue": "Symmetry and balance are key in Moroccan Zellige art - look for repeating motifs.",
                "artifact": "Zellige tile fragment"
            },
            {
                "title": "The Hidden Phrase",
                "description": "Decode the ancient script to reveal a traditional Moroccan saying.",
                "type": "word",
                "clue": "A celestial body that guides travelers.",
                "answer": "star",
                "artifact": "Ancient manuscript page"
            }
        ],
        "fes": [
            {
                "title": "The Tannery Challenge",
                "description": "Arrange the dye vats in the correct sequence to create the famous Fes leather.",
                "type": "sequence",
                "solution": ["yellow", "red", "green", "blue"],
                "clue": "Follow the process from lightest to darkest dyes as traditionally done in the tanneries.",
                "artifact": "Traditional leather pouch"
            },
            {
                "title": "The Pottery Master",
                "description": "Select the correct tools to create Fassi pottery in the right order.",
                "type": "sequence",
                "solution": ["clay", "wheel", "kiln", "glaze"],
                "clue": "Consider how raw clay transforms step by step into decorated pottery.",
                "artifact": "Blue Fassi pottery piece"
            },
            {
                "title": "The Metal Craft",
                "description": "Identify the authentic patterns used in traditional Fes metalwork.",
                "type": "selection",
                "options": ["Arabesque", "Kufic", "Geometric stars", "Floral motifs"],
                "correct": [0, 2, 3],
                "clue": "Focus on designs often seen on trays, lamps, and doors in Fes medina.",
                "artifact": "Decorative metal container"
            }
        ],
        "chefchaouen": [
            {
                "title": "The Blue Mystery",
                "description": "Find the original reason why Chefchaouen's buildings were painted blue.",
                "type": "choice",
                "options": [
                    "To keep mosquitoes away", 
                    "To symbolize the sky and heaven", 
                    "To attract tourists", 
                    "To keep buildings cool"
                ],
                "answer": 1,
                "clue": "Think of spiritual symbolism rather than practical purposes.",
                "artifact": "Blue pigment sample"
            },
            {
                "title": "The Berber Symbols",
                "description": "Match the Berber symbols with their meanings.",
                "type": "matching",
                "options": {
                    "ⵣ": "Free person",
                    "⵰": "Fertility",
                    "ⴶ": "Symmetery",
                    "ⴲ": "Wholeness"
                },
                "clue": "These symbols are often seen in Berber tattoos, jewelry, and textiles."
                ,"artifact": "Berber jewelry piece"
            }
        ],
        "sahara": [
            {
                "title": "Desert Navigation",
                "description": "Use the stars to find your way across the Sahara to the oasis.",
                "type": "path",
                "solution": ["north", "east", "east", "south"],
                "clue": "The North Star will guide you first, and remember — oases often lie southward.",
                "artifact": "Ancient desert map"
            },
            {
                "title": "The Rhythm of the Desert",
                "description": "Create the correct rhythm pattern of traditional Gnawa music.",
                "type": "path",
                "solution": ["slow", "repeat", "medium", "fast"],
                "clue": "Start slow, repeat, then quicken the pace like a Gnawa trance rhythm.",
                "artifact": "Krakebs (metal castanets)"
            },
            {
                "title": "The Nomad's Tent",
                "description": "Arrange the elements of a traditional nomadic tent in the correct positions.",
                "type": "position",
                "solution": {"pole": "center", "carpet": "floor", "chest": "west", "tea_set": "east"},
                "clue": "Hospitality rules: tea is served facing east; valuables rest safely to the west.",
                "artifact": "Tuareg pendant"
            }
        ],
        "casablanca": [
            {
                "title": "Modern Art Styles",
                "description": "Identify which art styles influenced these Moroccan contemporary artists.",
                "type": "matching",
                "options": {
                    "Farid Belkahia": "Organic forms and traditional materials",
                    "Hassan Hajjaj": "Pop art and fashion photography",
                    "Lalla Essaydi": "Calligraphy and feminist themes",
                    "Mohamed Melehi": "Wave patterns and vibrant colors"
                },
                "clue": "Match each artist's hallmark motifs to their signature materials and themes.",
                "artifact": "Contemporary art"
            },
            {
                "title": "Architectural Timeline",
                "description": "Arrange these Casablanca buildings in the order they were constructed.",
                "type": "sequence",
                "solution": ["Mahkama du Pacha", "Habous Quarter", "Hassan II Mosque", "Morocco Mall"],
                "clue": "Start with historical landmarks before moving to modern marvels.",
                "artifact": "Architectural drawing"
            },
            {
                "title": "The Final Code",
                "description": "Using clues from all regions, decode the message that unlocks the final treasure.",
                "type": "code",
                "hint": "The best kingdom in the world!",
                "answer": "MOROCCO",
                "artifact": "Iron key to Moroccan cultural heritage"
            }
        ]
    }
    
    if region in puzzles and 0 <= puzzle_number < len(puzzles[region]):
        return puzzles[region][puzzle_number]
    else:
        return {
            "title": "Puzzle Not Found",
            "description": "This puzzle is not available yet.",
            "type": "error"
        }
artifacts = {"Zellige tile fragment": "zellige.png",
            "Traditional Moroccan box": "box.png",
            "Traditional leather pouch": "leather_pouch.png",
            "Blue Fassi pottery piece": "pottery_piece.jpg",
            "Decorative metal container": "container.jpg",
            "Blue pigment sample": "blue_paint.jpg",
            "Berber jewelry piece": "berber_jewel.jpg",
            "Ancient desert map": "old_map.jpg",
            "Krakebs (metal castanets)": "krakeb.jpg",
            "Tuareg pendant": "ornament.png",
            "Contemporary art": "painting.jpg",
            "Architectural drawing": "drawing.jpg",
            "Iron key to Moroccan cultural heritage": "key.png",
            "Ancient manuscript page": "amazigh_text.jpg",
            }

def render_puzzle(region):
    """Render the current puzzle for the region."""
    current_puzzle_index = st.session_state.progress[region]["current_puzzle"]
    
    # Check if all puzzles are completed
    if current_puzzle_index >= st.session_state.progress[region]["total_puzzles"]:
        st.success(f"You have completed all puzzles in {region.capitalize()}!")
        return
    
    # Load puzzle data
    puzzle = load_puzzle_data(region, current_puzzle_index)
    
    # Display puzzle
    st.subheader(puzzle["title"])
    st.write(puzzle["description"])
    
    # Initialize answer in session state if not exists
    puzzle_key = f"{region}_puzzle_{current_puzzle_index}"
    if puzzle_key not in st.session_state:
        st.session_state[puzzle_key] = {"answered": False, "correct": False, "attempt": None}
    
    # If puzzle already answered correctly, show success message
    if st.session_state[puzzle_key]["answered"] and st.session_state[puzzle_key]["correct"]:
        st.success("Puzzle solved correctly! You found a new artifact.")
        st.image("assets/images/artifacts/" + artifacts[puzzle["artifact"]], caption=f"Artifact: {puzzle['artifact']}")
        
        if st.button("Continue to next puzzle"):
            advance_puzzle(region)
            # Reset the current puzzle state
            st.session_state[puzzle_key] = {"answered": False, "correct": False, "attempt": None}
            st.rerun()
        return
    
    # Render different puzzle types
    if puzzle["type"] == "matching":
        render_matching_puzzle(puzzle, puzzle_key, region)
    elif puzzle["type"] == "pattern":
        render_pattern_puzzle(puzzle, puzzle_key, region)
    elif puzzle["type"] == "word":
        render_word_puzzle(puzzle, puzzle_key, region)
    elif puzzle["type"] == "sequence":
        render_sequence_puzzle(puzzle, puzzle_key, region)
    elif puzzle["type"] == "choice":
        render_choice_puzzle(puzzle, puzzle_key, region)
    elif puzzle["type"] == "selection":
        render_selection_puzzle(puzzle, puzzle_key, region)
    elif puzzle["type"] == "path":
        render_path_puzzle(puzzle, puzzle_key, region)
    elif puzzle["type"] == "position":
        render_position_puzzle(puzzle, puzzle_key, region)
    elif puzzle["type"] == "code":
        render_code_puzzle(puzzle, puzzle_key, region)
    else:
        st.error("Unknown puzzle type")
    
    # Hint button
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Get Hint"):
            use_hint()
            if "hint" in puzzle:
                st.info(f"Hint: {puzzle['hint']}")
            elif "clue" in puzzle:
                st.info(f"Hint: {puzzle['clue']}")
            else:
                st.info("Think about the cultural significance of the elements in this puzzle.")

def render_matching_puzzle(puzzle, puzzle_key, region):
    """Render a matching puzzle."""
    options = list(puzzle["options"].keys())
    values = list(puzzle["options"].values())
    
    # Randomize the order of values for the user to match
    if f"{puzzle_key}_shuffled" not in st.session_state:
        shuffled_values = values.copy()
        random.shuffle(shuffled_values)
        st.session_state[f"{puzzle_key}_shuffled"] = shuffled_values
    
    shuffled_values = st.session_state[f"{puzzle_key}_shuffled"]
    
    # Create a dictionary to store matches
    if f"{puzzle_key}_matches" not in st.session_state:
        st.session_state[f"{puzzle_key}_matches"] = {option: "" for option in options}
    
    # Display the matching interface
    st.write("Match each item on the left with its description on the right:")
    
    for i, option in enumerate(options):
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write(f"**{option}**")
        with col2:
            st.session_state[f"{puzzle_key}_matches"][option] = st.selectbox(
                f"Matches with...",
                [""] + shuffled_values,
                key=f"match_{region}_{i}"
            )
    
    # Check answer button
    if st.button("Submit Matches", key=f"submit_{puzzle_key}"):
        correct = True
        for option, expected_value in puzzle["options"].items():
            if st.session_state[f"{puzzle_key}_matches"][option] != expected_value:
                correct = False
                break
        
        st.session_state[puzzle_key]["answered"] = True
        st.session_state[puzzle_key]["correct"] = correct
        
        if correct:
            st.success("Correct! You solved the puzzle.")
            add_artifact("assets/images/artifacts/" + artifacts[puzzle["artifact"]])
        else:
            st.error("That's not quite right. Try again!")
        
        st.rerun()

def render_pattern_puzzle(puzzle, puzzle_key, region):
    """Render a pattern matching puzzle."""
    # Simulate pattern tiles with numbers
    if f"{puzzle_key}_selected" not in st.session_state:
        st.session_state[f"{puzzle_key}_selected"] = []
    
    st.write("Click the tiles in the correct order to complete the pattern:")
    
    # Display tiles
    cols = st.columns(4)
    for i in range(4):
        with cols[i]:
            tile_key = f"tile_{region}_{i}"
            # Check if this tile is already selected
            st.image(f"assets/images/tiles/tile_{i+1}.png", caption=f"Tile {i+1}")
            if i+1 in st.session_state[f"{puzzle_key}_selected"]:
                st.button(f"Tile {i+1} ✓", key=tile_key, disabled=True)
            else:
                if st.button(f"Tile {i+1}", key=tile_key):
                    st.session_state[f"{puzzle_key}_selected"].append(i+1)
    
    # Display current selection
    st.write("Your current pattern:")
    st.write(" → ".join([f"Tile {tile}" for tile in st.session_state[f"{puzzle_key}_selected"]]))
    
    # Reset selection button
    if st.button("Reset Selection", key=f"reset_{puzzle_key}"):
        st.session_state[f"{puzzle_key}_selected"] = []
        st.rerun()
    
    # Check pattern when all tiles are selected
    if len(st.session_state[f"{puzzle_key}_selected"]) == len(puzzle["solution"]):
        correct = st.session_state[f"{puzzle_key}_selected"] == puzzle["solution"]
        
        st.session_state[puzzle_key]["answered"] = True
        st.session_state[puzzle_key]["correct"] = correct
        
        if correct:
            st.success("Correct! You solved the pattern.")
            add_artifact("assets/images/artifacts/" + artifacts[puzzle["artifact"]])
        else:
            st.error("That's not the right pattern. Try again!")
            st.session_state[f"{puzzle_key}_selected"] = []
        
        st.rerun()

def render_word_puzzle(puzzle, puzzle_key, region):
    """Render a word puzzle."""
    st.write("Decode the ancient script to reveal the hidden word:")
    
    # Display a placeholder for the "ancient script"
    st.image("assets/images/artifacts/star_amazigh.jpg", caption="Ancient script symbols")
    
    # Input field for answer
    answer = st.text_input("Enter your answer:", key=f"answer_{region}")
    
    # Check answer button
    if st.button("Submit Answer", key=f"submit_{puzzle_key}"):
        correct = answer.lower().strip() == puzzle["answer"].lower()
        
        st.session_state[puzzle_key]["answered"] = True
        st.session_state[puzzle_key]["correct"] = correct
        st.session_state[puzzle_key]["attempt"] = answer
        
        if correct:
            st.success("Correct! You decoded the message.")
            add_artifact("assets/images/artifacts/" + artifacts[puzzle["artifact"]])
        else:
            st.error("That's not the right word. Try again!")
        
        st.rerun()

def render_sequence_puzzle(puzzle, puzzle_key, region):
    """Render a sequence ordering puzzle."""
    items = puzzle["solution"].copy()
    
    # Initialize shuffled items if not already done
    if f"{puzzle_key}_shuffled" not in st.session_state:
        shuffled = items.copy()
        random.shuffle(shuffled)
        st.session_state[f"{puzzle_key}_shuffled"] = shuffled
    
    shuffled_items = st.session_state[f"{puzzle_key}_shuffled"]
    
    # Initialize selected sequence
    if f"{puzzle_key}_sequence" not in st.session_state:
        st.session_state[f"{puzzle_key}_sequence"] = []
    
    st.write("Arrange these items in the correct sequence:")

    # Display items to select
    cols = st.columns(len(shuffled_items))
    for i, item in enumerate(shuffled_items):
        with cols[i]:
            if item in st.session_state[f"{puzzle_key}_sequence"]:
                st.button(f"{item} ✓", disabled=True, key=f"seq__{i}")
            else:
                if st.button(f"{item}", key=f"seq__{i}"):
                    st.session_state[f"{puzzle_key}_sequence"].append(item)
    
    # Display current sequence
    st.write("Your current sequence:")
    st.write(" → ".join(st.session_state[f"{puzzle_key}_sequence"]))
    
    # Reset button
    if st.button("Reset Sequence", key=f"reset_{puzzle_key}"):
        st.session_state[f"{puzzle_key}_sequence"] = []
        st.rerun()
    
    # Check if sequence is complete
    if len(st.session_state[f"{puzzle_key}_sequence"]) == len(puzzle["solution"]):
        correct = st.session_state[f"{puzzle_key}_sequence"] == puzzle["solution"]
        
        st.session_state[puzzle_key]["answered"] = True
        st.session_state[puzzle_key]["correct"] = correct
        
        if correct:
            st.success("Correct! You arranged the sequence perfectly.")
            add_artifact("assets/images/artifacts/" + artifacts[puzzle["artifact"]])
        else:
            st.error("That's not the right sequence. Try again!")
            st.session_state[f"{puzzle_key}_sequence"] = []
        
        st.rerun()

def render_choice_puzzle(puzzle, puzzle_key, region):
    """Render a multiple choice puzzle."""
    st.write("Select the correct answer:")
    
    # Radio buttons for options
    answer = st.radio(
        "Choose one:",
        puzzle["options"],
        key=f"choice_{region}"
    )
    
    # Submit button
    if st.button("Submit Answer", key=f"submit_{puzzle_key}"):
        selected_index = puzzle["options"].index(answer)
        correct = selected_index == puzzle["answer"]
        
        st.session_state[puzzle_key]["answered"] = True
        st.session_state[puzzle_key]["correct"] = correct
        
        if correct:
            st.success("Correct! You chose the right answer.")
            add_artifact("assets/images/artifacts/" + artifacts[puzzle["artifact"]])
        else:
            st.error("That's not the right answer. Try again!")
        
        st.rerun()

def render_selection_puzzle(puzzle, puzzle_key, region):
    """Render a multiple selection puzzle."""
    st.write("Select all that apply:")
    
    # Initialize selection state if not exists
    if f"{puzzle_key}_selection" not in st.session_state:
        st.session_state[f"{puzzle_key}_selection"] = [False] * len(puzzle["options"])
    
    # Checkboxes for options
    for i, option in enumerate(puzzle["options"]):
        st.session_state[f"{puzzle_key}_selection"][i] = st.checkbox(
            option,
            value=st.session_state[f"{puzzle_key}_selection"][i],
            key=f"select_{region}_{i}"
        )
    
    # Submit button
    if st.button("Submit Selection", key=f"submit_{puzzle_key}"):
        selected = [i for i, selected in enumerate(st.session_state[f"{puzzle_key}_selection"]) if selected]
        correct = sorted(selected) == sorted(puzzle["correct"])
        
        st.session_state[puzzle_key]["answered"] = True
        st.session_state[puzzle_key]["correct"] = correct
        
        if correct:
            st.success("Correct! You selected all the right options.")
            add_artifact("assets/images/artifacts/" + artifacts[puzzle["artifact"]])
        else:
            st.error("That's not the right selection. Try again!")
        
        st.rerun()

def render_path_puzzle(puzzle, puzzle_key, region):
    """Render a path finding puzzle."""
    st.write("Select the directions to navigate correctly:")
    
    if puzzle["title"] == "The Rhythm of the Desert":
        directions = ["slow", "fast", "medium", "repeat"]
    else:
        directions = ["north", "east", "south", "west"]

    # Initialize path if not exists
    if f"{puzzle_key}_path" not in st.session_state:
        st.session_state[f"{puzzle_key}_path"] = []
    
    # Display current path
    st.write("Your current path:")
    path_text = " → ".join(st.session_state[f"{puzzle_key}_path"]) if st.session_state[f"{puzzle_key}_path"] else "No directions selected yet"
    st.write(path_text)
    
    # Direction buttons
    cols = st.columns(4)
    for i, direction in enumerate(directions):
        with cols[i]:
            if st.button(direction.capitalize(), key=f"dir_{region}_{i}"):
                st.session_state[f"{puzzle_key}_path"].append(direction)
                st.rerun()
    
    # Reset path button
    if st.button("Reset Path", key=f"reset_{puzzle_key}"):
        st.session_state[f"{puzzle_key}_path"] = []
        st.rerun()
    
    # Check path if it matches the solution length
    if len(st.session_state[f"{puzzle_key}_path"]) == len(puzzle["solution"]):
        correct = st.session_state[f"{puzzle_key}_path"] == puzzle["solution"]
        
        st.session_state[puzzle_key]["answered"] = True
        st.session_state[puzzle_key]["correct"] = correct
        
        if correct:
            st.success("Correct! You found the right path.")
            add_artifact("assets/images/artifacts/" + artifacts[puzzle["artifact"]])
        else:
            st.error("That's not the right path. Try again!")
            st.session_state[f"{puzzle_key}_path"] = []
        
        st.rerun()

def render_position_puzzle(puzzle, puzzle_key, region):
    """Render a positioning puzzle."""
    st.write("Place each item in its correct position:")
    
    items = list(puzzle["solution"].keys())
    positions = list(set(puzzle["solution"].values()))
    
    # Initialize positions if not exists
    if f"{puzzle_key}_positions" not in st.session_state:
        st.session_state[f"{puzzle_key}_positions"] = {item: "" for item in items}
    
    # Create select boxes for each item
    for item in items:
        st.session_state[f"{puzzle_key}_positions"][item] = st.selectbox(
            f"Place the {item} at:",
            [""] + positions,
            key=f"pos_{region}_{item}"
        )
    
    # Submit button
    if st.button("Submit Arrangement", key=f"submit_{puzzle_key}"):
        correct = True
        for item, expected_pos in puzzle["solution"].items():
            if st.session_state[f"{puzzle_key}_positions"][item] != expected_pos:
                correct = False
                break
        
        st.session_state[puzzle_key]["answered"] = True
        st.session_state[puzzle_key]["correct"] = correct
        
        if correct:
            st.success("Correct! You placed everything in the right position.")
            add_artifact("assets/images/artifacts/" + artifacts[puzzle["artifact"]])
        else:
            st.error("That's not the right arrangement. Try again!")
        
        st.rerun()

def render_code_puzzle(puzzle, puzzle_key, region):
    """Render a code/password puzzle."""
    st.write("Enter the final code using clues from your journey:")
    
    # Display artifacts collected as clues
    if st.session_state.artifacts_collected:
        st.write("Your collected artifacts:")
        for artifact in st.session_state.artifacts_collected:
            st.write(f"- {artifact}")
    
    # Input field for the code
    code = st.text_input("Enter the code:", key=f"code_{region}")
    
    # Submit button
    if st.button("Submit Code", key=f"submit_{puzzle_key}"):
        correct = code.upper().strip() == puzzle["answer"].upper()
        
        st.session_state[puzzle_key]["answered"] = True
        st.session_state[puzzle_key]["correct"] = correct
        
        if correct:
            st.success("Correct! You cracked the final code.")
            add_artifact("assets/images/artifacts/" + artifacts[puzzle["artifact"]])
        else:
            st.error("That's not the right code. Try again!")
        
        st.rerun()
