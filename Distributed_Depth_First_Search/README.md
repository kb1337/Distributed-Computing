# Token Based Distributed Depth First Search With Finite State Machine

## Example Graph

<hr>

<img src="https://user-images.githubusercontent.com/73403802/146685382-76660f83-8e52-4588-8288-7dfb619f8011.png" height=170></img>

```python
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
```

### Output

```
Rank 4, neighs: [3]
Waiting message...
Parent 3
Visit 1, Current Token [0, 1, 2, 3, 4]
Check neighs [3] if all visited
Every neighbors are visited
Rank 4 finished, sent token to parent 3
Token [0, 1, 2, 3, 4] goes to 3


Rank 7, neighs: [0, 1, 6]
Waiting message...
Parent 6
Visit 1, Current Token [0, 1, 2, 3, 4, 5, 6, 7]
Check neighs [0, 1, 6] if all visited
Every neighbors are visited
Rank 7 finished, sent token to parent 6
Token [0, 1, 2, 3, 4, 5, 6, 7] goes to 6


Rank 6, neighs: [2, 3, 5, 7]
Waiting message...
Parent 5
Visit 1, Current Token [0, 1, 2, 3, 4, 5, 6]
Check neighs [2, 3, 5, 7] if all visited
Token [0, 1, 2, 3, 4, 5, 6] goes to 7
Waiting message...
Visit 2, Current Token [0, 1, 2, 3, 4, 5, 6, 7]
Check neighs [2, 3, 5, 7] if all visited
Every neighbors are visited
Rank 6 finished, sent token to parent 5
Token [0, 1, 2, 3, 4, 5, 6, 7] goes to 5


Rank 5, neighs: [3, 6]
Waiting message...
Parent 3
Visit 1, Current Token [0, 1, 2, 3, 4, 5]
Check neighs [3, 6] if all visited
Token [0, 1, 2, 3, 4, 5] goes to 6
Waiting message...
Visit 2, Current Token [0, 1, 2, 3, 4, 5, 6, 7]
Check neighs [3, 6] if all visited
Every neighbors are visited
Rank 5 finished, sent token to parent 3
Token [0, 1, 2, 3, 4, 5, 6, 7] goes to 3


Rank 3, neighs: [2, 4, 5, 6]
Waiting message...
Parent 2
Visit 1, Current Token [0, 1, 2, 3]
Check neighs [2, 4, 5, 6] if all visited
Token [0, 1, 2, 3] goes to 4
Waiting message...
Visit 2, Current Token [0, 1, 2, 3, 4]
Check neighs [2, 4, 5, 6] if all visited
Token [0, 1, 2, 3, 4] goes to 5
Waiting message...
Visit 3, Current Token [0, 1, 2, 3, 4, 5, 6, 7]
Check neighs [2, 4, 5, 6] if all visited
Every neighbors are visited
Rank 3 finished, sent token to parent 2
Token [0, 1, 2, 3, 4, 5, 6, 7] goes to 2


Rank 2, neighs: [1, 3, 6]
Waiting message...
Parent 1
Visit 1, Current Token [0, 1, 2]
Check neighs [1, 3, 6] if all visited
Token [0, 1, 2] goes to 3
Waiting message...
Visit 2, Current Token [0, 1, 2, 3, 4, 5, 6, 7]
Check neighs [1, 3, 6] if all visited
Every neighbors are visited
Rank 2 finished, sent token to parent 1
Token [0, 1, 2, 3, 4, 5, 6, 7] goes to 1


Rank 1, neighs: [0, 2, 7]
Waiting message...
Parent 0
Visit 1, Current Token [0, 1]
Check neighs [0, 2, 7] if all visited
Token [0, 1] goes to 2
Waiting message...
Visit 2, Current Token [0, 1, 2, 3, 4, 5, 6, 7]
Check neighs [0, 2, 7] if all visited
Every neighbors are visited
Rank 1 finished, sent token to parent 0
Token [0, 1, 2, 3, 4, 5, 6, 7] goes to 0


Rank 0, neighs: [1, 7]
Token [0] goes to 1
Waiting message...
Visit 1, Current Token [0, 1, 2, 3, 4, 5, 6, 7]
Check neighs [7] if all visited
Every neighbors are visited
Root, all done [0, 1, 2, 3, 4, 5, 6, 7]
```

<hr>
