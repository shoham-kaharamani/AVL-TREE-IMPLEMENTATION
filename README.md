# AVL Tree Implementation in Python

A complete, object-oriented implementation of a self-balancing binary search tree (**AVL Tree**) from scratch in Python. This project demonstrates strict adherence to theoretical time complexities for core dictionary operations while dynamically maintaining tree balance through rotations.

## Features
* **Self-Balancing Logic:** Implements full tree rebalancing (`rebalanceAVL`) via Single and Double rotations (`rotate_left`, `rotate_right`) to guarantee $O(\log n)$ height.
* **Flexible Inserters:** Supports optimized entry insertion starting from either the `root` node or tracking the `max` node for sequential data efficiency.
* **Full Dictionary Operations:** Includes robust Node searching, Successor discovery, Leaf/Internal node deletion, and In-Order traversal serialization (`avl_to_array`).
* **Analytical Metrics:** Features internal tracking for Amir's balance factor calculation, evaluating the structural symmetry of the tree dynamically.

## Technologies Used
* **Python** (Object-Oriented Programming)

## Code Structure
* `AVLNode`: Represents a distinct key-value node tracking its relative height, parent pointers, and localized balance status.
* `AVLTree`: Main interface executing balanced state mutations and metric collections.
