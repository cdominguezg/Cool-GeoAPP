import os

from dependency_injector import containers, providers

from app.dependency_injection.src.postal_code.postal_code_di import PostalCodeContainer
from app.dependency_injection.src.turnover.turnover_di import TurnoverContainer


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=[f"config_{os.getenv('STAGE') or 'dev'}.yml"])

    postal_code = providers.Container(
        PostalCodeContainer,
        config=config
    )

    turnover = providers.Container(
        TurnoverContainer,
        config=config
    )
