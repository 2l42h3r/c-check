from ccheck.domain.exercise.exercise_type import ExerciseType
from ccheck.services.exercise_factory import ExerciseFactoryService
from ccheck.domain.exercise.exercise import Exercise
from ccheck.services.shell import ShellService
from ccheck.utils.tokenizer_service import TokenizerService
from ccheck.utils.validation_utils_service import ValidationUtilsService


class ApplicationService:
    __shell_service: ShellService
    __exercise_factory_service: ExerciseFactoryService
    __tokenizer_service: TokenizerService
    __exercise: Exercise
    __validation_service: ValidationUtilsService

    def __init__(
        self,
        shell_service: ShellService,
        exercise_factory_service: ExerciseFactoryService,
        tokenizer_service: TokenizerService,
        validation_service: ValidationUtilsService,
    ) -> None:
        self.__shell_service = shell_service
        self.__exercise_factory_service = exercise_factory_service
        self.__tokenizer_service = tokenizer_service
        self.__validation_service = validation_service

    def __on_exercise_select(self, exercise_type: ExerciseType) -> None:
        self.__exercise = self.__exercise_factory_service.create_exercise(exercise_type)

    def run(self) -> None:
        self.__shell_service.print_exercise_list(self.__on_exercise_select)
        self.__shell_service.print_exercise_question(self.__exercise)

        solution = self.__shell_service.read_solution()
        tokens_cleaned = self.__validation_service.prepare_token_list(
            self.__tokenizer_service.tokenize(solution)
        )
        errors = self.__exercise.validate(tokens_cleaned)
        print(errors)
