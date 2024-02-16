
## Retrieve an object from its memory addres
```python
import ctypes
a = "hello world"
print(ctypes.cast(id(a), ctypes.py_object).value)
```

### Only in VS Code
Adding "#%%" to a line creates a jupyter cell

[IPython VS Code Tutorial](https://code.visualstudio.com/docs/python/jupyter-support-py)


<details><summary>Jupyter</summary>
Store magic

- `%store my_var`
- `%store -r` # retrieve vars
- `look for more`


</details>


### pip
* Check available versions for a package
`pip index versions package_name`

### useful functions

`pandas.crosstab()` : Compute a simple cross tabulation of two (or more) factors.


<details>
<summary>Dictionaries Upgraded</summary>


```python
class Map(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.iteritems():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.iteritems():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]
```


### Usage examples:

`m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])`
Add new key
`m.new_key = 'Hello world!'`
Or
`m['new_key'] = 'Hello world!'`
`print m.new_key`
`print m['new_key']`
# Update values
m.new_key = 'Yay!'
# Or
m['new_key'] = 'Yay!'
# Delete key
del m.new_key
# Or
del m['new_key']


```python
class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
```

`pip install dotmap`bash

</details>


### Libraries
- DotMap (dictionary with dot accesor: `dict['attr'] == dict.attr`) -> pip install dotmap
- IceCream: Never use print() to debug again


### To Do
- Learn module and package importing (including __init__.py)
