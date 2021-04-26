from dotenv import load_dotenv
from pathlib import Path


def env_definitions():
    """
    Load local dot.env file
    ### CHECK ENV.EXAMPLE FILE ###
    :return: All environment variables loaded in env
    """
    load_dotenv(verbose=True)
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
