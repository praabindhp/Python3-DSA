class CustomList:
    def __init__(self) -> None:
        self.list = []

    def add_element(self, element):
        # Implement this function
        if element not in self.list:
            self.list.append(element)
        return

    def remove_element(self, element):
        # Implement this function
        if element in self.list:
            self.list.remove(element)
        return

    def get_length(self):
        # Implement this function
        return len(self.list)
    