# jupyter_environment_provisioner

A Jupyter server extension to provision the `os.environ` with environment variables. Useful for programatically provisioning a BinderHub instance.

## Usage

1. Install the server extension
2. Add the appropriate names/patterns to the `allowed_names` or `allowed_patterns` traits.
3. Post to the `/environment_provisioner/set` endpoint with JSON body

