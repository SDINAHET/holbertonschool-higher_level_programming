#!/usr/bin/python3
import marshal

def get_names_from_pyc(filename):
    with open(filename, 'rb') as f:
        magic = f.read(16)  # Skip magic number and timestamp
        code = marshal.load(f)  # Load the code object

    return [name for name in dir(code) if not name.startswith('__')]

if __name__ == "__main__":
    names = get_names_from_pyc('/tmp/hidden_4.pyc')
    for name in sorted(names):
        print(name)
