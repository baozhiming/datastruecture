import sys
import yaml
from pathlib import Path
from typing import Dict


class PathUtil:
    root_path = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    @staticmethod
    def init(root_path):
        sys.path.append(root_path)
        PathUtil.root_path = root_path

    @staticmethod
    def get_abs_path(path: str) -> str:
        return str(Path(PathUtil.root_path) / path)


class ConfigUtil:
    def __init__(self):
        pass

    @staticmethod
    def load(config_path: str) -> Dict:
        try:
            config = yaml.safe_load(open(config_path).read())
        except FileNotFoundError:
            raise FileNotFoundError(f"cluster configuration file ({config_path}) does not exist")
        except yaml.parser.ParserError as e:
            raise Exception(e)
        except yaml.scanner.ScannerError as e:
            raise Exception(e)
        return config
