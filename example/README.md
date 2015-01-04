Silly example
=============

Now this is a really silly example that serves only to prove that this thing
actually works. Please don't take this as an example of how you should
organize your project or fashion your makefile.


Dependencies
------------

You need the following two executables on your `PATH`:

- `qr` from the Python package `qrcode` (see the note below)
- `closure-compiler` i.e. the Google Closure Compiler


Usage
-----

Once you have `closure-compiler` and `qr` (see the note below) on your `PATH`
you can run this example as follows:

    $ cd path/to/oldfart
    $ bin/ve_up
    $ cd example
    $ python -m oldfart --serve-from build/dist

After which you can point your browser to `http://localhost:8000/index.html`.


### Note about qrcode ###

Unfortunately the Python package `qrcode` is not yet Python 3
compatible. Therefore you need to install it separately outside Oldfart's
virtual environment.
