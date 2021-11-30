from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


# Root sends the first message.
if rank == 0:
    print(f"Rank: {rank}")
    comm.send(rank, rank + 1, tag=1337)
else:
    msg = comm.recv(source=rank - 1, tag=1337)
    print(f"Rank: {rank}, Message: {msg}")
    if (rank + 1) < size:
        comm.send(rank, rank + 1, tag=1337)
