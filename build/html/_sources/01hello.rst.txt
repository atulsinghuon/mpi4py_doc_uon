Hello world
===========

This example talks about basics of rank and number of processes in MPI.

.. code-block:: python

    from mpi4py import MPI
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    print('My rank is ',rank)


The following output is expected. (Assuming the ``--ntasks-per-node`` was assigned as 4.)

.. code-block:: bash

    My rank is 2
    My rank is 3
    My rank is 1
    My rank is 0


The variable ``comm`` holds the group of processes that can commmunicate with each other, with the default
being ``MPI.COMM_WORLD``. The ``rank`` variable on the other hand represents the particular process within the communicator. 
Indicating that the processors within ``ntasks-per-node`` can be assigned chunks of code separately, to perform parallel calculations. 

This is explored in further sections. 