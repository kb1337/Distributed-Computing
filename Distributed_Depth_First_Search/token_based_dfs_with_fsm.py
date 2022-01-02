from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

TOKEN = 0  # Message tag
parent = -1

msg = [-1, -1]  # [rank, token]
neighs = []
token = []
visit_count = 0

NOT_VISITED = 0
VISITED = 1
OVER = 2
state = NOT_VISITED

PRINT_DETAILS = True


adjacency_matrix = np.array(
    [
        [0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 1, 0],
    ],
    dtype=int,
)

neighbors = adjacency_matrix[rank]

for i in range(0, size):
    if neighbors[i] == 1:
        neighs.append(i)

print(f"\n\nRank {rank}, neighs: {neighs}")


def act00():
    global token, parent, state, msg, rank, visit_count
    visit_count += 1
    print("Waiting message...") if PRINT_DETAILS else 0
    msg = comm.recv(source=MPI.ANY_SOURCE, tag=TOKEN)

    token = msg[1]
    if parent == -1:  # First time visit
        parent = msg[0]  # Set Parent
        print(f"Parent {parent}") if PRINT_DETAILS else 0
        token.append(rank)

    print(f"Visit {visit_count}, Current Token {token}") if PRINT_DETAILS else 0

    next_node = -1
    print(f"Check neighs {neighs} if all visited") if PRINT_DETAILS else 0
    for node in neighs:  # Find next node to visit
        if node not in token:
            next_node = node
            break

    if next_node != -1:  # Next node found
        msg[0], msg[1] = rank, token
        print(f"Token {msg[1]} goes to {next_node}") if PRINT_DETAILS else 0
        comm.send(msg, dest=next_node, tag=TOKEN)
    else:
        print("Every neighbors are visited")
        state = VISITED


def act10():
    global token, msg, parent, rank, state
    if rank == 0:  # All done
        print("Root, all done", msg[1])
    else:  # Return to parent
        print(f"Rank {rank} finished, sent token to parent {parent}")
        msg[0] = rank
        print(f"Token {msg[1]} goes to {parent}") if PRINT_DETAILS else 0
        comm.send(msg, dest=parent, tag=TOKEN)
    state = OVER


fsm_tab = np.array([[act00], [act10]])

if rank == 0:  # ROOT starts DFS
    parent = 0
    next_node = neighs.pop(0)  # First neighbor of ROOT
    msg[0] = rank  # rank
    msg[1] = [rank]  # token

    print(f"Token {msg[1]} goes to {next_node}") if PRINT_DETAILS else 0
    comm.send(msg, dest=next_node, tag=TOKEN)

while state != OVER:
    fsm_tab[state][TOKEN]()  # 2 states 1 message type
