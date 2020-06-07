`Python`_ client for `Consul.io`_
==================================

This is service register/discovery for `Python`_ based on the `python-consul`_ library.

Usage is the same as the `standard API`_ except that it auto fills service info.

Example
-------

.. code:: python
    from discovery import Registry

    registry = Registry()
    registry.register('my-service-name', 8080)


Installation
------------

::

        pip install consul-discovery


.. _Consul.io: http://www.consul.io/
.. _python-consul: http://python-consul.readthedocs.org
.. _standard API:
    http://python-consul.readthedocs.org/en/latest/#api-documentation
