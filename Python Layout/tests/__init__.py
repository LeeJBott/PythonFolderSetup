# The __init__.py file is a special Python file that serves a specific purpose depending on where it's 
# placed within your project's directory structure.

# __init__.py files serve to mark directories as Python packages and can also be used to define the behavior 
# of importing the package and its modules. Each package directory should typically have its own __init__.py file,
# and these files may contain different content depending on the specific needs of the package or module.

# example
from .package import Package
from .test import Test