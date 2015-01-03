import os
import re
import subprocess


__all__ = ['NOOP', 'SUCCESS', 'FAIL', 'Maker']


NOTHING_DONE = 1
SUCCESS = 2
NO_RULE = 3
FAILURE = 4


class Maker(object):

    def __init__(self, project_dir='.', makefile='Makefile'):
        self.project_dir = os.path.abspath(project_dir)
        self.makefile = os.path.abspath(os.path.join(project_dir, makefile))

    def make(self, target):
        """Runs `make(1)` on `target` and returning a tuple `(status, output)`
        where `status` is one of:

        - `make.SUCCESS`: the target was successfully generated
        - `make.NOTHING_DONE`: the target was already up-to-date
        - `make.NO_RULE`: there is no rule to build the requested target
        - `make.FAILURE`: `make(1)` exited otherwise with a non-zero error code

        Returned `output` contains always the mixed output from `stdout` and
        `stderr`.
        """
        try:
            capture = subprocess.check_output(
                ['make', '--makefile=' + self.makefile, target],
                cwd=self.project_dir, stderr=subprocess.STDOUT,
                universal_newlines=True)
            if re.match(r"make: `[^']*' is up to date.", capture):
                return (NOTHING_DONE, capture)
            else:
                return (SUCCESS, capture)
        except subprocess.CalledProcessError as e:
            if re.match(r"make: \*\*\* No rule to make target `{:s}'.  Stop."
                        .format(target), e.output):
                return (NO_RULE, e.output)
            else:
                return (FAILURE, e.output)
