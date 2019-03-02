from setuptools import setup
from wxwidgets import __version__

setup(
    name='wxwidgets',
    version=__version__,
    description='wxpython based gui elements',
    author='Christian',
    author_email='christian1193@web.com',
    packages=['wxwidgets'],
    install_requires=['wxPython', 'webcolors']
)
