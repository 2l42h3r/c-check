from dependency_injector import containers, providers

from ccheck.config import Config
from ccheck.services.application import ApplicationService
from ccheck.services.shell import ShellService
from ccheck.utils.tokenizer_service import TokenizerService


class Container(containers.DeclarativeContainer):
    config = providers.Factory(Config)

    shell_service = providers.Singleton(ShellService, config=config)

    application_service = providers.Singleton(
        ApplicationService, shell_service=shell_service
    )

    tokenizer_service = providers.Factory(TokenizerService, config=config)
