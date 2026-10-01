#!/usr/bin/env python3


class Plant:

    class PlantStats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def grow_called(self) -> None:
            self._grow_count += 1

        def age_called(self) -> None:
            self._age_count += 1

        def show_called(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        growth_rate: float | None = None
    ) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate
        self.stats = Plant.PlantStats()

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        if self.growth_rate is not None:
            self.height += self.growth_rate

        self.stats.grow_called()

    def age(self) -> None:
        for i in range(20):
            self.age_days += 1

        self.stats.age_called()

    def show(self) -> None:
        self.stats.show_called()

        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age_days} days old"
        )


class Flower(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str
    ) -> None:
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

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = trunk_diameter
        self._shade_count = 0

    def produce_shade(self) -> None:
        self._shade_count += 1

        print(
            f"Tree {self.name} now produces a shade of "
            f"{round(self.height, 1)}cm long and "
            f"{round(self.trunk_diameter, 1)}cm wide."
        )

    def show_shade_stats(self) -> None:
        print(f"{self._shade_count} shade")

    def show(self) -> None:
        super().show()

        print(
            f"Trunk diameter: "
            f"{round(self.trunk_diameter, 1)}cm"
        )


class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        harvest_season: str,
        nutritional_value: int
    ) -> None:
        super().__init__(name, height, age_days)

        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()

        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str
    ) -> None:
        super().__init__(name, height, age_days, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


def main() -> None:

    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )

    print("")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)

    print("")
    print("[asking the rose to grow and bloom]")

    rose.growth_rate = 8.0
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    oak.show_shade_stats()

    print("")
    print("[asking the oak to produce shade]")

    oak.produce_shade()
    display_statistics(oak)
    oak.show_shade_stats()

    print("")

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.growth_rate = 30.0
    sunflower.show()

    print("")
    print("[make sunflower grow, age and bloom]")

    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("")

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
