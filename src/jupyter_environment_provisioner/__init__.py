from .app import EnvironmentApp


def _jupyter_server_extension_points():
    """
    Returns a list of dictionaries with metadata describing
    where to find the `_load_jupyter_server_extension` function.
    """
    return [{"module": "jupyter_environment_provisioner", "app": EnvironmentApp}]
