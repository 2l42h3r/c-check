from ccheck.domain.exercise_type import ExerciseType
from ccheck.services.shell import ShellService


class ApplicationService:
    __shell_service: ShellService

    def __init__(self, shell_service: ShellService) -> None:
        self.__shell_service = shell_service

    def __on_exercise_select(self, exercise_type: ExerciseType) -> None:
        print(exercise_type)

    def run(self) -> None:
        self.__shell_service.print_exercise_list(self.__on_exercise_select)
