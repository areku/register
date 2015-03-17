from register import __version__

from setuptools import setup

setup(
    name="register",
    author="Alexander Weigl",
    author_email="alexander.weigl@student.kit.edu",
    version=__version__,
    homepage="https://github.com/areku/register",
    description="registry for functions and classes",
    py_modules=["register"],

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: MIT License",
    ],

    long_description="""
    registry
    --------

    """
)