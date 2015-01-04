"""
Oldfart is a HTTP server that can generate requested resources on-demand
using `make(1)` on the background.

You might want to use Oldfart as a development server. It would fit especially
well if you're already using `make(1)` to build your project the artifacts of
which are eventually served as static resources over HTTP.
"""

from setuptools import setup

setup(
    name = 'Oldfart',
    version = '0.1.0',
    url = 'http://github.com/soija/oldfart',
    license = 'BSD',
    author = 'Matti Hänninen',
    author_email = 'soija@itsme.soy',
    description = 'Serve make artefacts over HTTP',
    long_description = __doc__,
    package_dir = {'': 'py'},
    packages = ['oldfart'],
    zip_safe = True,
    platforms = 'any',
    install_requires = [],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
    ],
    entry_points = '''
    [console_scripts]
    oldfart=oldfart:main
    ''')
