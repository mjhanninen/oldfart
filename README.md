Oldfart
=======

**Oldfart** is a HTTP server that can generate requested resources on-demand
using `make(1)` on the background.

You might want to use Oldfart as a development server. It would fit especially
well if you're already using `make(1)` to build your project the artifacts of
which are eventually served as static resources over HTTP.

Oldfart is not a production server. In fact it is vulnerable to an injection
attack so **never expose Oldfart to an untrusted interface**.


Usage
-----

In the simplest case you serve your resources directly form the root of your
project and `Makefile` is also situated there. In that case:

    $ cd path/to/your/project
    $ oldfart
    Serving "path/to/your/project" through 127.0.0.1:8000

Let's assume a more complicated case where the resources are served from the
directory `build/dist/` inside the project via the port 8080.

    $ cd path/to/your/project
    $ oldfart --serve-from=build/dist/ --port=8080
    Serving "path/to/your/project/build/dist" through 127.0.0.1:8080

Please see the working example in `example/` directory for further
information.


Installation
------------

The usual drill:

    $ cd path/to/oldfart
    $ python setup.py install


Development
-----------

To activate the virtual environment just run the `ve_up` script:

    $ bin/ve_up
    Virtual environment activated. Press ^D to exit.
    $ python
    Python 3.4.2 (default, Oct 19 2014, 17:52:17)
    [GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.51)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import oldfart
    >>>

In case the virtual environment hasn't been set up before the script does that
and installs the dependencies listed in `requirements.txt` and
`dev_requirements.txt` if any. The latter is meant only for the developer's
own personal workflow tooling (e.g. `ipython) and is outside the source
control. The dependencies are updated every time the requirement files change.

The activation script also amends the project source directory (`./py/`) to
the front of `PYTHONPATH`.
