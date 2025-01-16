import streamlit as st
import matplotlib.pyplot as plt

class Interface():

    # Streamlit UI
    st.title("Beer Pong Simulation")
    st.write("Die Becher sind in einem engen Dreieck angeordnet. Getroffene Becher bleiben rot.")
    # Initialisiere den Status der Becher im Session State
    if "becher_status" not in st.session_state:
        st.session_state.becher_status = {
            'becher1': False,
            'becher2': False,
            'becher3': False,
            'becher4': False,
            'becher5': False,
            'becher6': False
        }

    # Funktion zum Zeichnen des Spielfeldes
    def draw_beer_pong_game(becher_status):
        fig, ax = plt.subplots()
        ax.set_xlim(-4, 4)  # Grenzen für die x-Achse
        ax.set_ylim(-6, 6)  # Grenzen für die y-Achse

        # Becherpositionen angepasst, sodass sie sich nicht überschneiden
        positions = {
            'becher1': (2.5, -1.5),  # Linker oberer Becher
            'becher2': (0, 4),       # Mittlerer oberer Becher
            'becher3': (2.5, 1.5),   # Rechter oberer Becher
            'becher4': (-2.5, -1.5), # Linker unterer Becher
            'becher5': (-4, 0),      # Mittlerer unterer Becher
            'becher6': (-2.5, 1.5),  # Rechter unterer Becher
        }

        # Zeichne jeden Becher
        for becher, position in positions.items():
            color = 'blue'  # Standardfarbe
            if becher_status[becher]:
                color = 'red'  # Getroffener Becher wird rot
            ax.add_patch(plt.Circle(position, 1, color=color, ec="black"))

        ax.set_aspect('equal', 'box')
        plt.axis('off')
        st.pyplot(fig)


    # Buttons, um Treffer zu simulieren
    for becher in st.session_state.becher_status.keys():
        if st.button(f"{becher.capitalize()} getroffen"):
            st.session_state.becher_status[becher] = True  # Markiere Becher als getroffen

    # Zeichne die aktuelle Spielszene
    draw_beer_pong_game(st.session_state.becher_status)
