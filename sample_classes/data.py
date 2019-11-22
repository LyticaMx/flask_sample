class Data:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.name} {self.last_name}'
