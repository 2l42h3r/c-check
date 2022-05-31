from typing import List, Callable

from ccheck.config import Config
from ccheck.domain.exercise_type import ExerciseType


class ShellService:
    __exercise_list: List[Config.ExerciseDict]

    def __init__(self, config: Config) -> None:
        self.__exercise_list = config.exercise_config

    def __is_input_valid_exercise_number(self, typed: str) -> bool:
        try:
            val = int(typed)
            if val <= len(self.__exercise_list):
                return True
            return False
        except ValueError:
            return False

    def print_exercise_list(
        self, on_exercise_select: Callable[[ExerciseType], None]
    ) -> None:
        print("Dostępne rodzaje zadań:")
        for index, exercise in enumerate(self.__exercise_list, start=1):
            print(index, ") ", exercise["name"])
        typed = input("Wybierz numer zadania: ")

        # handle custom error

        if self.__is_input_valid_exercise_number(typed):
            on_exercise_select(self.__exercise_list[int(typed) - 1]["exercise"])
