#!/usr/bin/python3

import winsound
import time

# Jouer une note avec une fréquence et une durée
def play_note(frequency, duration):
    winsound.Beep(frequency, duration)
    time.sleep(duration / 1000)  # Pause pour la durée de la note

# Mélodie améliorée de James Bond
def play_007_theme():
    # Introduction
    play_note(466, 300)  # Bb4
    play_note(523, 300)  # C5
    play_note(587, 300)  # D5
    time.sleep(0.1)
    play_note(466, 300)  # Bb4
    play_note(523, 300)  # C5
    play_note(587, 300)  # D5
    time.sleep(0.1)

    # Partie principale (plus dynamique)
    play_note(523, 200)  # C5
    play_note(523, 200)  # C5
    play_note(523, 200)  # C5
    play_note(587, 200)  # D5
    play_note(523, 200)  # C5
    play_note(466, 300)  # Bb4
    time.sleep(0.1)

    # Répéter la partie principale pour une meilleure impression
    play_note(523, 200)  # C5
    play_note(523, 200)  # C5
    play_note(523, 200)  # C5
    play_note(587, 200)  # D5
    play_note(523, 200)  # C5
    play_note(466, 300)  # Bb4
    time.sleep(0.1)

# Appeler la fonction pour jouer le thème
play_007_theme()
