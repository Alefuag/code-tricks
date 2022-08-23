
## Retrieve an object from its memory addres
import ctypes
a = "hello world"
print(ctypes.cast(id(a), ctypes.py_object).value)


## Learn module and package importing (including __init__.py)

''' pip
## Check available versions for a package ##
pip index versions package_name

'''

