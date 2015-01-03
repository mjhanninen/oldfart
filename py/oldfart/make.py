import os
import re
import subprocess


__all__ = ['NOOP', 'SUCCESS', 'FAIL', 'Maker']


NOOP = 1
SUCCESS = 2
FAIL = 3


class Maker(object):

    def __init__(self, project_dir='.', makefile='Makefile'):
        self._project_dir = os.path.abspath(project_dir)
        self._makefile = os.path.abspath(os.path.join(project_dir, makefile))

    def make(self, resource):
        """Runs `make(1)` on `resource` and returning a tuple `(status, output)`
        where `status` is one of:

        - `make.SUCCESS`: the resource was successfully generated
        - `make.NOOP`: the resource was already up-to-date
        - `make.FAIL`: `make(1)` exited with a non-zero error code.

        Returned `output` contains always the mixed output from `stdout` and
        `stderr`.
        """
        try:
            capture = subprocess.check_output(
                ['make', '--makefile=' + self._makefile, resource],
                cwd=self._project_dir, stderr=subprocess.STDOUT,
                universal_newlines=True)
            if re.match(r"make: `[^']*' is up to date.", capture) is not None:
                return (NOOP, capture)
            else:
                return (SUCCESS, capture)
        except subprocess.CalledProcessError as e:
            return (FAIL, e.output)
