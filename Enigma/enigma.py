# EnigmaClone Encoding
# Step 1: Input
# Step 2: Plug Board
# Step 3: Rotors (Twice)
# Step 4: Plug Board Again
# Step 5: Output Light

from .rotor import Rotor

import string


class EnigmaMachine(object):

    """Setup an EnigmaClone Machine.

    Include just a one-way mapping on the plug board. For example if you wish to plug 'a' and 'q', pass in {'a':'q'}.

    :param rotors: Selected Rotor instances for this EnigmaClone Machine.
    :type rotors: list of Rotor
    :param dict plug_board: Map characters on the plug board

    """

    def __init__(self, rotors, plug_board):
        self.plug_board = plug_board
        self.num_plugs = len(plug_board)
        self._fix_plug_board()

        self.selected_rotors = rotors
        self.num_rotors = len(rotors)
        self._check_rotors()

        self.lights = list(string.ascii_lowercase)
        self.input_keys = list(string.ascii_lowercase)

    def _fix_plug_board(self):
        # Check one character is only connected to one other character at most
        for key in self.plug_board:
            value = self.plug_board[key]
            if value in self.plug_board and self.plug_board[value] != key:
                raise RuntimeError("%s is connected to two characters, which is not allowed!" % value)

        # Ensure reverse of all plug board combinations is present correctly to allow two-way indexing
        keys = list(self.plug_board)
        for key in keys:
            value = self.plug_board[key]
            self.plug_board[value] = key

    def _check_rotors(self):
        for rotor in self.selected_rotors:
            if not isinstance(rotor, Rotor):
                raise RuntimeError("All rotors must be of type Rotor.")
            rotor.is_valid_rotor()

    def transform_input(self, input_char):
        """Pass input character through the plug board, twice through rotors, and through plug board again.

        :param str input_char: Pressed input key
        :returns: transformed character
        :rtype: str

        """
        # Send input through the plug board
        plug_board_output = self.plug_board.get(input_char, input_char)
        rotor_output = rotor_input = plug_board_output

        # Send the character through the rotors in one direction
        for rotor in self.selected_rotors:
            rotor_output = rotor.transform_input(rotor_input)
            rotor_input = rotor_output

        # Send the character through the rotors in the reverse order
        for rotor in self.selected_rotors[::-1]:
            rotor_output = rotor.transform_input(rotor_input)
            rotor_input = rotor_output

        # Send the character through the plug board again
        output_char = self.plug_board.get(rotor_output, rotor_output)
        return output_char


