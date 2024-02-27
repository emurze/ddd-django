from importlib import import_module

from django.apps import AppConfig
from django.apps.config import MODELS_MODULE_NAME
from django.utils.module_loading import module_has_submodule


class FlexibleAppConfig(AppConfig):
    models_parent_path = None

    def import_models(self) -> None:
        # Dictionary of models for this app, primarily maintained in the
        # 'all_models' attribute of the Apps this AppConfig is attached to.
        self.models = self.apps.all_models[self.label]

        if self.models_parent_path:
            submodule = "%s.%s" % (self.models_parent_path, MODELS_MODULE_NAME)
        else:
            submodule = MODELS_MODULE_NAME

        if module_has_submodule(self.module, submodule):
            models_module_name = "%s.%s" % (self.name, submodule)
            self.models_module = import_module(models_module_name)  # noqa
