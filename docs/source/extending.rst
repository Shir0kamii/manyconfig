Extend Manyconfig
#################

Adding a file format
====================

You can easily add support for a file format by adding a parser to Manyconfig.

Suppose you have a format with key/value pairs separated by an equal sign.
This is how you would add support for your format:

.. code-block:: python

    from manyconfig import format_parsers


    @format_parsers.add("key=value")
    def parse(file_object):
        config = {}
        for line in file_object:
            key, value = line.split("=")
            config[key] = value
        return config


    metaconfig = FileMetaConfig("key=value", "config")

You need to add the format parser before instanciating the FileMetaConfig.

Extend MetaConfig
=================

To extend the :class:`~manyconfig.config.MetaConfig` class, you need to
override the :meth:`~manyconfig.config.MetaConfig._load` method. It should
return a dictionnary.

You can also override the `__init__` method to capture arguments during
instanciation, but please forward keyword-arguments to `super`.
