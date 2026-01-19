from  collections.abc import  Iterable
import  random

def observe(value):
    try:
        _ = repr(value)
    except Exception:
        pass

def observe_deeply(value, seen=None):
    if seen is None:
        seen = set()
        
    if id(value) in seen:
        return 
    
    seen.add(id(value))
    observe(value)

    if isinstance(value, str):
        _ = len(value)
        for char in value:
            observe_deeply(char, seen)

    elif isinstance(value, dict):
        for k, v in value.items():
            observe_deeply(k, seen)
            observe_deeply(v, seen)

    elif isinstance(value, Iterable):
        for item in value:
            observe_deeply(item, seen)

def observe_or_not(value):
    if random.choice([True, False]):
        observe(value)
        print("ba")

def confirm_existence(*args):
     print(len(args) > 0)