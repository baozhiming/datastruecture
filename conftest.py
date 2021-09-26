import os
import sys
from pathlib import Path


PROJECT_ROOT = os.path.abspath(Path(os.path.dirname(__file__)))
sys.path.insert(0, PROJECT_ROOT)


from utils import PathUtil


PathUtil.init(root_path=PROJECT_ROOT)
