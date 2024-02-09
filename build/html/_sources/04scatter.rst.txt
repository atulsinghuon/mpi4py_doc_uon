Scatter
=======

Another collective form of communication is the scatter operation, where the data is broken up into different elements on each rank. This is effective when on operating on different variables using each rank, simultaneously.

.. code-block:: python

    from mpi4py import MPI
    import numpy as np

    comm = MPI.COMM_WORLD
    size = comm.Get_size() # new: gives number of ranks in comm
    rank = comm.Get_rank()

    numDataPerRank = 10  
    data = None
    if rank == 0:
        data = np.linspace(1,size*numDataPerRank,numDataPerRank*size)
        # when size=4 (using -n 4), data = [1.0:40.0]

    recvbuf = np.empty(numDataPerRank, dtype='d') # allocate space for recvbuf
    comm.Scatter(data, recvbuf, root=0)

    print('Rank: ',rank, ', recvbuf received: ',recvbuf)

This code constructs a data object using ``numDataPerRank`` to have 10 data points per rank multiplied by the size, which is generatured from number of ranks. Those data are then scattered to each rank in communicator. 

.. image:: scatter2.png
    
Scatter, as shown in the image above can also be used to send each data or a set of data to specific ranks as need be. This can be used to operate on each component of data at the same time, effectively reducing overall time to handle variables in parallel.



