import streamlit as st
import matplotlib.pyplot as plt
"""
TO DO:
-convert a cups into classes 
-they should be initialized outside the function
-initialize them with color blue as default and a position x y 
"""


class Cups():
    def __init__(self):



def one_interface():
    # Initialisiere den Status der Becher im Session State
    if "cup status" not in st.session_state:
        st.session_state.cup_status = {
            'becher1': False,
            'becher2': False,
            'becher3': False,
            'becher4': False,
            'becher5': False,
            'becher6': False
        }

    # Draw playingfield
    def draw_beer_pong_game(cup_status):
        fig, ax = plt.subplots()
        ax.set_xlim(-7, 7)  # Grenzen für die x-Achse
        ax.set_ylim(-4, 4)  # Grenzen für die y-Achse

        
        #fit cup positions, so they don´t intersect
        positions = {
            'becher1': (-4, 2.5),  #left up
            'becher2': (-1.5, 0),       #left middle 
            'becher3': (-4, -2.5),   #left bottom
            'becher4': (4, 2.5),  #right up
            'becher5': (1.5, 0),      #right middle
            'becher6': (4, -2.5),  #right bottom
        }

        # Draw cups 
        for becher, position in positions.items():
            color = 'blue'  # Standardfarbe
            if cup_status[becher]:
                color = 'red'  # Getroffener Becher wird rot
            ax.add_patch(plt.Circle(position, 1, color=color, ec="black"))

        ax.set_aspect('equal', 'box')
        plt.axis('off')
        st.pyplot(fig)


    # Buttons, um Treffer zu simulieren

    for becher in st.session_state.cup_status.keys():
        if st.button(f"{becher.capitalize()} getroffen"):
            st.session_state.cup_status[becher] = True  # Markiere Becher als getroffen
 
    # Zeichne die aktuelle Spielszene
    draw_beer_pong_game(st.session_state.cup_status)

one_interface()