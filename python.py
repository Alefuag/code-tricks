
## Retrieve an object from its memory addres

import ctypes
a = "hello world"
print(ctypes.cast(id(a), ctypes.py_object).value)


