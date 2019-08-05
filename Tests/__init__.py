import inspect
import os
import sys

current_dir = os.path.dirname(
    os.path.abspath(
        inspect.getfile(
            inspect.currentframe()
        )
    )
)

parent_dir = os.path.dirname(
    current_dir
)

project_dir = os.path.dirname(
    parent_dir
)

sys.path.insert(
    0,
    f"{ project_dir }/Python3"
)
