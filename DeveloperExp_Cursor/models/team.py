class Team:
    def __init__(self, name):
        self.name = name
        self.data = {}
        self.maturity_level = None

    def add_data(self, metric, value):
        self.data[metric] = value

    def set_maturity_level(self, level):
        self.maturity_level = level

    def get_data(self):
        return self.data

    def get_maturity_level(self):
        return self.maturity_level

    def __str__(self):
        return f"Team: {self.name}, Maturity: {self.maturity_level}, Data: {self.data}" 