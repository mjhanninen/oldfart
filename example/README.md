Silly example
=============

Now this is a really silly example that serves only to prove that this thing
actually works. Please don't take this as an example of how you should
organize your project or fashion your makefile.

Dependencies
------------

- [`qrcode` Python package][https://pypi.python.org/pypi/qrcode/5.0.1]
- [Google Closure Compiler][https://github.com/google/closure-compiler]

Usage
-----

Once you have `closure-compiler` on your `PATH` you can run this example as
follows:

    $ cd path/to/oldfart
    $ bin/ve_up
    $ cd example
    $ python -m oldfart --serve-from build/dist

After which you can point your browser to
[`http://localhost:8000/index.html`][http://localhost:8000/index.html].
