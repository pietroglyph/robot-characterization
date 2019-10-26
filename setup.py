import setuptools
import sys, subprocess
from datetime import date
from os.path import dirname, exists, join

setup_dir = dirname(__file__)
git_dir = join(setup_dir, ".git")
version_file = join(setup_dir, "version.py")

# Automatically generate a version.py based on the git version
if exists(git_dir):
    proc = subprocess.run(
        [
            "git",
            "rev-list",
            "--count",
            # Includes previous year's commits in case one was merged after the
            # year incremented. Otherwise, the version wouldn't increment.
            "--after=\"master@{" + str(date.today().year - 1) + "-01-01}\"",
            "HEAD"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    # If there is no master branch, the commit count defaults to 0
    if proc.returncode:
        commit_count = "0"
    else:
        commit_count = proc.stdout.decode("utf-8")

    # Version number: <year>.<# commits on master>
    version = str(date.today().year) + "." + commit_count.strip()

    # Create the version.py file
    with open(version_file, 'w') as fp:
        fp.write("# Autogenerated by setup.py\n__version__ = \"{0}\"".format(
            version))

if exists(version_file):
    with open(version_file, "r") as fp:
        exec(fp.read(), globals())
else:
    raise FileNotFoundError("No .git directory found")

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README_pypi.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='frc-characterization',
    version=__version__,
    author='Eli Barnett, Dustin Spicuzza',
    author_email='emichaelbarnett@gmail.com, dustin@virtualroadside.com',
    description='RobotPy Characterization Library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[
        'arm_characterization',
        'drive_characterization',
        'elevator_characterization',
        'logger_gui',
        'cli',
        'utils',
        'newproject',
        'robot'
    ],
    entry_points={'console_scripts': ['robotpy-characterization = cli.cli:main']},
    url='https://github.com/robotpy/robot-characterization',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'control',
        'frccontrol',
        'matplotlib',
        'pynetworktables>=2018.1.2',
        'statsmodels',
        'argcomplete',
        'console-menu',
        'mako',
    ],
    python_requires='>=3.7',
    include_package_data=True
)
