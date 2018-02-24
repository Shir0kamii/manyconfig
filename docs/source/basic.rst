Basic usage
###########

In most cases, building a MetaConfig is meant to be declarative: You only
declare and assemble objects, without the need to code the logic.

It integrates Marshmallow_, which is a plentyful of features in itself, so look
into it! (for example, use marshmallow for default values and runtime
transformations)

Single source
=============

For example, if you have a single json file named *foo.json* that contains your
configuration, you can retrieve it by running this snippet:

.. code-block:: python

    from manyconfig import FileMetaConfig
    metaconfig = FileMetaConfig("json", "foo.json")
    config = metaconfig.load()

Or, if your configuration resides in the environment and all its keys begins
with *APPLICATION_*, you could do:

.. code-block:: python

    from manyconfig import EnvironmentMetaConfig
    metaconfig = EnvironmentMetaConfig("APPLICATION_")
    config = metaconfig.load()


Multiple sources
================

Now, the two examples above can easily be dealt with without using Manyconfig.
But it's when there's multiple sources of configuration that it comes in handy.

Say, you use both of above configuration sources, with the environment
overriding the file. It's still easy enough but think about configurations of
programs like Bash, or flake8. They are far more complex but could be handled
with MetaConfig blocks.

Let's come back to our example and see how it looks:

.. code-block:: python

    from manyconfig import EnvironmentMetaConfig, FileMetaConfig, ManyConfig
    env_metaconfig = EnvironmentMetaConfig("APPLICATION_")
    file_metaconfig = FileMetaConfig("json", "foo.json")
    metaconfig = ManyConfig(file_metaconfig, env_metaconfig)
    config = metaconfig.load()


Validating configuration
========================

Even though it's not a dependency, Manyconfig is built with Marshmallow_ in
mind. You can define a Schema class and use it to validate the configuration.

This is integrated in Manyconfig so no need to do it yourself. Just pass the
instanciated schema to the MetaConfig block when you build it.


.. code-block:: python

    from manyconfig import FileMetaConfig
    from marshmallow import Schema
    from marshmallow.fields import Integer, String


    class ConfigSchema(Schema):
        database = String()
        verbosity_level = Integer()

    
    metaconfig = FileMetaConfig("json", "foo.json")
    config = metaconfig.load()
    # yields something like {"database": "sql://foo", "verbosity_level": 42}

.. _Marshmallow: http://marshmallow.readthedocs.io/
