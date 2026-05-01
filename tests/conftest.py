import os

def pytest_configure(config):
    """
    Hook to configure pytest before tests run.
    Here we ensure the 'logs' directory exists before the logging module
    attempts to create 'logs/automation.log' as defined in pytest.ini.
    """
    project_root = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(project_root, "logs")
    os.makedirs(log_dir, exist_ok=True)
