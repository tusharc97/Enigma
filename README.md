# Enigma
WW2 Enigma Machine Implementation and UI and code to break the encryption based on implementation used by Alan Turin et. al

Enigma Machine includes classes for:

    1) `EnigmaSetup` to create the Enigma Machine with set rotors and 
    plug board positions
    2) `Rotor` for each individual rotor

The Enigma Machine has 4 main components - Input Keys, Output lights, Plug Board, and Rotors.

Input Keys:

26 input keys corresponding to each letter of the alphabet to allow the
user to enter the encoded/decoded message.

Output Lights:

26 output lights corresponding to each letter of the alphabet to
indicate the decoded/encoded character based on the input.

Plug Board:

Allows the user to make 0-13 connections between 2 alphabets to swap
them. Each character can only be connected to at most one other character.

Rotors:

Each Rotor has a unique transformation and an internal counter. The
transformed character is based on the unique rotor connections and the
value of the counter. The user can pick up to 5 Rotors the selected
rotors function as a collective counter and increment from 0-26. Once
the first rotor has 26 rotations, it wraps around and the next rotor
gets a single increments and so on for all rotors.


Functionality:

Encoding:
    The user records the plug board setting and the order and initial
    value of rotors selected. Then, they type the input message one
    character at a time on the input keys. The input key is then swapped
    on the plug board if a connection exists for that character. The
    swapped character then moves through the rotors in order, being
    transformed after every rotor. The rotors are also incremented based
    on the previously discussed rules. The character then moves back
    through the rotors in reverse order. This character is then swapped
    at the plug board if a connection exists and the corresponding
    output light is illuminated.

Decoding:
    The user sets the plug board, order and initial counter value of the
    rotors to the same value the encoder recorded before encoding the
    message. The same process as defined in encoding occurs and the
    decoded character is illuminated in the output lights.


