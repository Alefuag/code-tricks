
## Retrieve an object from its memory addres
```python
import ctypes
a = "hello world"
print(ctypes.cast(id(a), ctypes.py_object).value)
```

### Only in VS Code
Adding "#%%" to a line creates a jupyter cell

[IPython VS Code Tutorial](https://code.visualstudio.com/docs/python/jupyter-support-py)




### pip
* Check available versions for a package
`pip index versions package_name`

### useful functions

`pandas.crosstab()` : Compute a simple cross tabulation of two (or more) factors.



```python
class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

```

### Libraries
- DotMap (dictionary with dot accesor: `dict['attr'] == dict.attr`) -> pip install dotmap
- IceCream: Never use print() to debug again


### To Do
- Learn module and package importing (including __init__.py)
