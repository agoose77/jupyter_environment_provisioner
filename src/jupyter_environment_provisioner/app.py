from jupyter_server.extension.application import ExtensionApp
from jupyter_server.utils import url_path_join
from .handlers import SetEnvironmentHandler

import re
from traitlets import Unicode, List, validate, TraitError


class EnvironmentProvisionerApp(ExtensionApp):
    # -------------- Required traits --------------
    name = "environment_provisioner"
    load_other_extensions = True

    allowed_names = List(Unicode(), config=True)
    allowed_patterns = List(Unicode(), config=True)

    @validate("allowed_patterns")
    def _valid_allowed_patterns(self, proposal):
        for name in proposal["value"]:
            try:
                re.compile(name)
            except re.PatternError:
                raise TraitError(f"Invalid regex pattern {name!r}")
        return proposal["value"]

    def initialize_handlers(self):
        self.handlers.append((url_path_join(self.name, "set"), SetEnvironmentHandler))
