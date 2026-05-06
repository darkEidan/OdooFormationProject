from abc import ABC, abstractmethod


class BaseMenu(ABC):

    def __init__(self, title: str):
        self.title = title
        self.options = {}  # {"1": ("Label", function)}

    def display(self):
        print(f"\n==== {self.title} ====")
        for key, (label, _) in self.options.items():
            print(f"{key}. {label}")
        # Adding the Exit choice
        print("0. Exit")

    def run(self):
        while True:
            self.display()

            choice = input("Select an option: ")

            if choice == "0":
                break

            action = self.options.get(choice)

            if action:
                _, func = action
                func()
            else:
                print("❌ Invalid choice")

    @abstractmethod
    def configure(self):
        pass
