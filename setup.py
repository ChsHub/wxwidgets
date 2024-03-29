import setuptools
from distutils.core import setup

from wxwidgets import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='wxwidgets',
    version=__version__,
    description='wxpython based gui elements',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='ChsHub',
    url="https://github.com/ChsHub/wxwidgets",
    packages=['wxwidgets'],
    install_requires=['wxPython'],
    license='MIT License',
    classifiers=['Programming Language :: Python :: 3']
)

# Upload commands
# C:\Python38\python.exe setup.py sdist bdist_wheel
# C:\Python38\python.exe -m twine upload dist/*
