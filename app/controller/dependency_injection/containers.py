from dependency_injector import containers, providers

from app.controller.dependency_injection.src.postal_code.postal_code_di import PostalCodeContainer


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])

    postal_code = providers.Container(
        PostalCodeContainer,
        config=config
    )
