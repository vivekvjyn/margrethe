Usage Examples
--------------

Basic Logging
~~~~~~~~~~~~~

Log messages using an instance of `Margrethe`:

.. code-block:: python

    from margrethe import Margrethe

    logger = Margrethe(log_dir='logs', width=80)
    logger("This is a log message.")

Progress Bar
~~~~~~~~~~~~

`Margrethe` class can also display a progress bar for iterative tasks:

.. code-block:: python

    from margrethe import Margrethe
    import time

    logger = Margrethe(log_dir='logs', width=80)
    total = 100
    for i in range(total + 1):
        logger.pbar(i, total)
        time.sleep(0.1)
