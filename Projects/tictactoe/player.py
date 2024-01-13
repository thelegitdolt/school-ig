class Player:
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def get_name(self):
        return self.name

    def get_state(self):
        return self.state

    def __eq__(self, other):
        if not type(other) == type(self):
            return False

        return (other.state == self.state) & (other.name == self.name)

