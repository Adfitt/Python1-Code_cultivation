# Object-Oriented Garden Systems — Python 1 (42 Barcelona)

*This repo was made by Adrian Fittipaldi (adrifitt / 42user)*

Second Python project of 42's new Common Core. The goal is to discover and practice Object-Oriented Programming by building a small garden system that evolves from simple plant objects into a more complete system with growth, encapsulation, inheritance, specialized plant types, and analytics.

Unlike the previous Python project, the exercises in this project focus on creating classes and objects, managing their state and behaviour, and progressively introducing more advanced Object-Oriented Programming concepts.

### Project rules

Your code must be written in Python 3.10+.

Your code must respect the flake8 linter standards.

Each exercise must be in its own file and directory.

Each exercise requires the use of classes.

Classes must use `PascalCase`.

Functions and variables must use `snake_case`.

Type hints are required for all functions and methods.

Type hints must be checked with `mypy`.

Input validation is not required unless explicitly requested by the exercise.

The program must always execute without errors.

The project uses a shebang at the beginning of Python files so that scripts can also be executed directly from the terminal.

### Stack

Python 3.10+

flake8 (code style and linting)

mypy (type checking with strict mode)

Object-Oriented Programming

### How to run and test

Each exercise can be executed directly with Python:

```bash
python3 ft_garden_intro.py
```

The project also uses a shebang:

```python
#!/usr/bin/env python3
```

This allows the files to be executed directly from the terminal.

First, give the file execution permissions:

```bash
chmod +x ft_garden_intro.py
```

Then it can be executed with:

```bash
./ft_garden_intro.py
```

So both methods are valid:

```bash
python3 ft_garden_intro.py
```

or:

```bash
./ft_garden_intro.py
```

The exercises use:

```python
if __name__ == "__main__":
    main()
```

so that the main program runs when the file is executed directly.

### Style and typing check

Before submitting, the code is checked with `flake8` and `mypy --strict`.

For example:

```bash
flake8 ft_garden_intro.py
```

`flake8` checks that the code follows the project's style requirements and reports formatting and code-quality issues.

For type checking:

```bash
mypy --strict ft_garden_intro.py
```

`mypy --strict` checks that the type hints are correctly used throughout the code.

Both checks are part of the project's development workflow. The subject requires type hints and specifies that they must be checked with `mypy`.

For a complete check of an exercise, both commands can be run:

```bash
flake8 ft_garden_intro.py
mypy --strict ft_garden_intro.py
```

EX3, for example, was checked after fixing its `flake8` indentation errors, and `mypy` reported no problems.

### Project structure

**ex0 / `ft_garden_intro.py`**

Introduces the basic structure of a Python program using simple variables to store a plant's name, height, and age. It also introduces `if __name__ == "__main__":`.

**ex1 / `ft_garden_data.py`**

Introduces the `Plant` class. Each plant stores its name, height, and age, and the `show()` method displays its information. The exercise introduces classes, instances, attributes, methods, `self`, and `__init__`.

**ex2 / `ft_plant_growth.py`**

Adds behaviour to `Plant`. The `grow()` method increases the plant's height and `age()` increases its age. The exercise simulates seven days of growth and calculates the total growth during the week. Different plant types can have different growth rates.

**ex3 / `ft_plant_factory.py`**

Creates plants directly with all their initial information and stores multiple plant instances in a list. The exercise uses at least five different plants: Rose, Oak, Cactus, Sunflower, and Fern.

**ex4 / `ft_garden_security.py`**

Introduces encapsulation and controlled access to plant data. Height and age are stored internally using `_height` and `_age`, while `get_height()`, `get_age()`, `set_height()`, and `set_age()` control access and modification. Negative values are rejected.

**ex5 / `ft_plant_types.py`**

Introduces inheritance and specialized plant types:

- `Flower` adds `color` and `bloom()`.
- `Tree` adds `trunk_diameter` and `produce_shade()`.
- `Vegetable` adds `harvest_season` and `nutritional_value`.

The exercise uses `super()` to reuse the functionality inherited from `Plant` and avoid duplicating common code.

**ex6 / `ft_garden_analytics.py`**

Introduces more advanced Object-Oriented Programming concepts:

- A `staticmethod` to check whether an age is greater than one year.
- A `classmethod` to create an anonymous plant.
- `Seed`, which inherits from `Flower`.
- `PlantStats`, a nested class that tracks calls to `grow()`, `age()`, and `show()`.
- Additional statistics for `Tree` through `produce_shade()`.
- An external `display_statistics()` function that works with different plant types.

The inheritance chain introduced in this exercise includes:

```text
Plant
└── Flower
    └── Seed
```

The statistics system is shared through inheritance, allowing the external statistics function to work with different types of plants.

### Main concepts learned

This project progressively introduces Object-Oriented Programming concepts rather than introducing everything at once.

**Classes and instances**

A class defines the structure and behaviour of objects, while an instance is a concrete object created from that class.

```python
rose = Plant("Rose", 25, 30)
```

Here, `Plant` is the class and `rose` is an instance of that class.

**State and behaviour**

The project distinguishes between the data stored by an object and the operations that modify or display that data.

```text
State:
name
height
age_days
growth_rate

Behaviour:
grow()
age()
show()
```



**Encapsulation**

EX4 introduces controlled access to internal data using getters and setters. The class becomes responsible for protecting its own state and rejecting invalid values.

**Inheritance**

EX5 introduces a common `Plant` base class and specialized subclasses:

```text
             Plant
          /    |     \
      Flower  Tree  Vegetable
```

This avoids duplicating common plant functionality.

**`super()`**

`super()` is used when a child class needs the functionality of its parent and then adds its own behaviour.

For example, `Flower` can reuse the `Plant` constructor and then add its own `color` attribute.

**Static and class methods**

EX6 introduces `staticmethod` for operations that do not depend on a particular plant instance, and `classmethod` for creating instances through the class itself.

**Nested classes and statistics**

`PlantStats` is implemented as a nested class inside `Plant`. Each plant gets its own statistics for `grow()`, `age()`, and `show()`, while `Tree` adds a specific statistic for `produce_shade()`.

### Project status

🟢 **Completed**

All exercises from EX0 to EX6 are implemented, including the final analytics system introduced in `ft_garden_analytics.py`.