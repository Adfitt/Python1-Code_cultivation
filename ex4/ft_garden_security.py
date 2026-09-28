#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name.capitalize()

        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age_days < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age_days

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"""{self.name} Error, height can´t be negative
Height update rejected""")
            return False

        self._height = height
        return True

    def get_age(self) -> int:
        return self._age

    def set_age(self, age_days: int) -> bool:
        if age_days < 0:
            print(f"""{self.name}: Error, Age can´t be negative
Age update rejected""")
            return False

        self._age = age_days
        return True

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")


def main() -> None:

    rose = Plant("rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    rose.show()
    print()

    if rose.set_height(25.0):
        print(f"Height update: {rose.get_height()}cm")

    if rose.set_age(30):
        print(f"Age update: {rose.get_age()} days")

    print()

    rose.set_height(-20)
    rose.set_age(-500)

    print()

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
