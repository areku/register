register
========


.. image:: https://travis-ci.org/areku/register.svg
    :target: https://travis-ci.org/areku/register

.. image:: https://pypip.in/download/register/badge.svg
    :target: https://pypi.python.org/pypi//register/
    :alt: Downloads

.. image:: https://pypip.in/version/register/badge.svg
    :target: https://pypi.python.org/pypi/register/
    :alt: Latest Version


.. image:: https://pypip.in/py_versions/register/badge.svg
    :target: https://pypi.python.org/pypi/register/
    :alt: Supported Python versions

.. image:: https://pypip.in/implementation/register/badge.svg
    :target: https://pypi.python.org/pypi/register/
    :alt: Supported Python implementations

.. image:: https://pypip.in/status/register/badge.svg
    :target: https://pypi.python.org/pypi/register/
    :alt: Development Status

.. image:: https://pypip.in/wheel/register/badge.svg
    :target: https://pypi.python.org/pypi/register/
    :alt: Wheel Status

.. image:: https://pypip.in/egg/register/badge.svg
    :target: https://pypi.python.org/pypi/register/
    :alt: Egg Status

.. image:: https://pypip.in/format/register/badge.svg
    :target: https://pypi.python.org/pypi/register/
    :alt: Download format

.. image:: https://pypip.in/license/register/badge.svg
    :target: https://pypi.python.org/pypi/register/
    :alt: License



Python Module for providing a simple register for function and classes with support of meta data.

.. code-block::
    Author: Alexander Weigl
    License: MIT

Getting Started
---------------

Install with pip::

    $ pip install --user register


Use it::

>>> from register import Registry
>>> r = Registry()
>>> @r
>>> def abc(): pass
>>> r.lookup("abc")
