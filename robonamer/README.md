# RoboNamer

A response to [this exercise](https://exercism.io/tracks/python/exercises/robot-name/) from the internets.

> Manage robot factory settings.
>
> When robots come off the factory floor, they have no name.
>
> The first time you boot them up, a random name is generated in the format of two uppercase letters followed by three digits, such as RX837 or BC811.
>
> Every once in a while we need to reset a robot to its factory settings, which means that their name gets wiped. The next time you ask, it will respond with a new random name.
>
> The names must be random: they should not follow a predictable sequence. Random names means a risk of collisions. Your solution must ensure that every existing robot has a unique name.

## Approach and outcome

I used this as an opportunity to try out test-driven development. I used pytest installed under pipenv. This could be further improved by using pytest-mock to introduce mocking to the tests, particularly those which involve reading from and writing to names.txt.

The script was successful and meets all the conditions set out above. However it will slow down over time as more used names are added to names.txt. Perhaps a better solution exists...

Some lessons learned:
- Pipenv is great
- TDD is a useful approach and reveals potential problems early on
- There's no point in testing methods that only use simple parts of the standard library - that job belongs to Python core devs!
- Pytest > unittest
- I need to get my head around mocking
- Writing a fleshed-out ReadMe like this one is probably a good idea too

## Update January 2022

- found I had not implemented the reset part of the scenario, so added that to `robonamer.py`
- found more concise way to generate names
- testing adds names to `names.txt` thereby removing potential valid names from the pool. It would be better if I mocked this out somehow.