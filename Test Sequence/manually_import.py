# Copyright 2017 by Adil Iqbal.
# All rights reserved.
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.

import os
import sys


def manually_import(name):
    """Find, manually import, and return a python module.

    This function is intended to help import modules that are
    not part of the 'Bio' package. For an example of how to use
    this function, please look at its use in the
    'test_testseq.py' file in the 'Tests' folder.
    """
    # Find the path from 'biopython' folder.
    name = name.split(".")
    name[-1] += ".py"
    module_path = os.getcwd()
    module_path = os.path.split(module_path)
    if module_path[1] == "Tests":
        module_path = os.path.join(module_path[0], name.pop(0))
    else:
        raise ImportError("Must call 'manually_import' from inside 'Tests' folder.")
    for i, step in enumerate(name):
        module_path = os.path.join(module_path, step)

    # Manually import and return module.
    name = name[-1][:-3]
    if 2.7 <= float(sys.version[0:3]) < 3.0:
        # Python version 2.7
        import imp
        return imp.load_source(name, module_path)
    elif sys.version_info[1] < 5:
        # Python version 3.3 and 3.4
        from importlib.machinery import SourceFileLoader
        return SourceFileLoader(name, module_path).load_module()
    elif sys.version_info[1] >= 5:
        # Python version 3.5+
        from importlib.util import spec_from_file_location, module_from_spec
        spec = spec_from_file_location(name, module_path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    else:
        raise ImportError("Unsupported python version: %s" % sys.version)
