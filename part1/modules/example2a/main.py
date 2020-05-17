"""This file is an example of how python imports a module"""
import os
import types
import sys


module_name = 'module1'
module_file = 'module1_source.py'
module_path = '.'

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

# read source from file
with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()

# create module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

# set ref in sys.modules
sys.modules[module_name] = mod

# compile source code
code = compile(source_code, filename=module_abs_file_path, mode='exec')

exec(code, mod.__dict__)
# mod.__dict__ indicates where the variables will go

# import mod

mod.hello()
