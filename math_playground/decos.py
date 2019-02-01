"""Module to hold useful decorators"""

def cast_args(*types):
    """Casts arguments to specified type
    
    If None is supplied, then argument is left alone

    >>> @cast_arg(None, int)
    ... def print_types(arg1, arg2):
    ...     print(f'arg1 type = {type(arg1)}')
    ...     print(f'arg2 type = {type(arg2)}')
    ...
    >>> print_types('1', '1')
    arg1 type = <class 'str'>
    arg2 type = <class 'int'>
    """
    def decorator(func):
        def new_func(*args, **kwds):
            new_args = []        
            for (arg, new_type) in zip(args, types):
                if new_type is None:
                    new_args.append(arg)
                else:
                    new_args.append(new_type(arg))
            return func(*new_args, **kwds)
        return new_func
    return decorator