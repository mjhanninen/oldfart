Oldfart
-------

**Oldfart** is a Make-over-HTTP. It is an HTTP server that builds the
requested resources with with Make as necessary.


Development
===========

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
own personal tooling (e.g. `ipython) and is outside the source control. The
dependencies are updated every time the requirement files change.

The activation script also amends the project source directory (`./py/`) to
the front of `PYTHONPATH`.
