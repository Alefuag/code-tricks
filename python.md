
## Retrieve an object from its memory addres
```python
import ctypes
a = "hello world"
print(ctypes.cast(id(a), ctypes.py_object).value)
```

### Only in VS Code
Adding "#%%" to a line creates a jupyter cell

[IPython VS Code Tutorial](https://code.visualstudio.com/docs/python/jupyter-support-py)

### Learn module and package importing (including __init__.py)

### pip
* Check available versions for a package
`pip index versions package_name`


