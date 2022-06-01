from ccheck.domain.exercise.exercise_type import ExerciseType
from ccheck.services.exercise_factory import ExerciseFactoryService
from ccheck.domain.exercise.exercise import Exercise
from ccheck.services.shell import ShellService


class ApplicationService:
    __shell_service: ShellService
    __exercise_factory_service: ExerciseFactoryService
    __exercise: Exercise

    def __init__(
        self,
        shell_service: ShellService,
        exercise_factory_service: ExerciseFactoryService,
    ) -> None:
        self.__shell_service = shell_service
        self.__exercise_factory_service = exercise_factory_service

    def __on_exercise_select(self, exercise_type: ExerciseType) -> None:
        self.__exercise = self.__exercise_factory_service.create_exercise(exercise_type)
        print(self.__exercise.__class__)

    def run(self) -> None:
        self.__shell_service.print_exercise_list(self.__on_exercise_select)
