#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth_rates: float | None = None) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_days = age_days
        self.growth_rates = growth_rates

    def grow(self) -> None:
        if self.growth_rates is not None:
            self.height += self.growth_rates

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)},cm, "
              f"{self.age_days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age_days: int, color: str) -> None:
        super().__init__(name, height, age_days)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age_days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self.height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int, harv_sea: str,
                 nutri_val: int, growth_rate: float) -> None:
        super().__init__(name, height, age_days, growth_rate)
        self.harv_sea = harv_sea
        self. nutri_val = nutri_val

    def age(self) -> None:
        super().age()
        self.nutri_val += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harv_sea}")
        print(f"Nutritional value: {self.nutri_val}")


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oat to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("tomato", 5, 10, "april", 0, 2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
