qqlolapi: QQ LoL Esports Data API Wrapper
=========================================

qqlolapi is a python package that allows access to the undocumented API
of the League of Legends Esports section of QQ, which allows access to
match details of competitive matches in the Chinese `LPL
<http://lol.esportspedia.com/wiki/LPL/2016_Season/Spring_Season>`_.

Installation
------------

qqlolapi is currently not available at PyPI until core development is
100% finished. Until then, you can use pip to install the development version:

.. code-block:: bash

    $ pip install --upgrade https://github.com/flakeee/qqlolapi/archive/master.zip

Please notice that qqlolapi was made for Python 3.
Legacy support for Python 2 will follow later.

Documentation
-------------
There's no documentation available for qqlolapi yet. Until then, use
the source code to learn how to use the ``match`` and ``series`` endpoints.

License
-------

The source code of qqlolapi is licensed by
`the GNU LGPLv3 <https://github.com/flakeee/praw/blob/master/COPYING>`_.

Legal notice
------------

The API used by qqlolapi is undocumented and not made for public use.
This wrapper was made to dynamically create scoreboards in wiki
markup for `Esportspedia <http://lol.esportspedia.com>`_. Please
respect that the data wasn't released to the public through a public
API and Tencent can restrict access to the data/API used by qqlolapi.