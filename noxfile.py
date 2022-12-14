"""
About Nox: https://nox.thea.codes/en/stable/

noxfile.py Examples:

- https://github.com/pypa/pipx/blob/main/noxfile.py
"""
import os

import nox  # type: ignore

os.environ.update({"PDM_IGNORE_SAVED_PYTHON": "1"})

PYTHON_ALL_VERSIONS = ["3.7", "3.8", "3.9", "3.10"]
PYTHON_DEFAULT_VERSION = "3.10"


@nox.session(python=PYTHON_ALL_VERSIONS)
def test(session):
    session.run("pdm", "install", "-G", "dev", external=True)
    if session.python == "3.10":  # generate coverage report
        session.run(
            "pytest", "tests", "--cov", "src", "--cov-report", "xml:/tmp/coverage.xml"
        )
    else:
        session.run("pytest", "tests")
