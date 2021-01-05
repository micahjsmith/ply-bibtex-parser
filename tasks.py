from invoke import task

PKG_PATH = "ply_bibtex_parser"


@task
def test(c):
    """Run the test suite"""
    c.run(f"pytest tests", pty=True)


@task
def black(c, check=False, diff=False):
    """Run Black auto-formatter, optionally with --check or --diff"""
    check_flag, diff_flag = "", ""
    if check:
        check_flag = "--check"
    if diff:
        diff_flag = "--diff"
    c.run(f"black {check_flag} {diff_flag} tasks.py {PKG_PATH} tests")


@task
def isort(c, check=False, diff=False):
    check_flag, diff_flag = "", ""
    if check:
        check_flag = "-c"
    if diff:
        diff_flag = "--diff"
    c.run(f"isort {check_flag} {diff_flag} .")


@task
def flake8(c):
    c.run(f"flake8 tasks.py {PKG_PATH} tests")


@task
def lint(c):
    isort(c, check=True)
    black(c, check=True)
    flake8(c)
