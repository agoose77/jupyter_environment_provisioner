from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import (
    ExtensionHandlerMixin,
)
import tornado
import os
import re


class SetEnvironmentHandler(ExtensionHandlerMixin, JupyterHandler):
    @tornado.web.authenticated
    def post(self):
        model = self.get_json_body()

        patterns = [re.escape(p) for p in self.config.allowed_names]
        patterns.extend(self.config.allowed_patterns)

        if not model:
            return

        for name, value in model.items():
            if not any(re.match(p, name) for p in self.config.allowed_patterns):
                continue

            os.environ[name] = value

            self.log.info(f"Setting environment variable {name!r}")
