import streamlit as st


def main_interface():

    # Streamlit UI
    st.title("Beer Pong Simulation")
    st.write("Fill up the cups and place them into the holder, when finished press 'READY'")
    
    if st.button("Ready"):
        print("Ready")
        return 1

    