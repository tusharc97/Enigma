# Rotor class


class Rotor(object):
    def __init__(self, connections):
        self.connections = connections
        self.current_position = 0

    def click(self, num_rotations):
        # Click Rotor ahead by one position
        pass

    def transform_input(self, input_char):
        # Transform rotor input according to rotor position
        pass

    def is_valid_rotor(self):
        pass
