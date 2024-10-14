# Singly Linked List in Python

A simple implementation of a singly linked list with various utility functions.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Installation

You can install the package via pip:

```bash
pip install singly_linked_list
```

## Usage
Here’s a quick example of how to use the SinglyLinkList class:

```
from singly_linked_list import SinglyLinkList

# Create a new linked list
linked_list = SinglyLinkList()

# Add elements
linked_list.push(10)  # Add to front
linked_list.append(20) # Add to end
linked_list.insert(10, 15) # Insert after 10

# Print the list
print(linked_list.printList())  # Output: [15, 10, 20]

# Remove an element
linked_list.remove(10)
print(linked_list.printList())  # Output: [15, 20]
```

## Features
- Add Nodes: push(data), append(data), insert(after_element, data)
- Remove Nodes: remove(element), delete()
- Search: search(key), count(key)
- Traversal: printList(), length(), getNth(n), getNthFromLast(n)
- Utilities: isPalindrome(), checkLoop(), lengthOfLoop(), uniqueSorted()
- Modify List: reverseList(), segregateEvenOdd()
- Merging Lists: mergeTwoLists(l1, l2)

## API Reference
The SinglyLinkList class provides methods for manipulating linked lists as described in the features section. Each method has its own functionality:

- Initialization: SinglyLinkList()

- Add Nodes:
  - `push(data):` Add a new node at the beginning.
  - `append(data):` Add a new node at the end.
  - `insert(after_element, data):` Insert a new node after a specified element.

- Remove Nodes:
  - `remove(element):` Remove the first occurrence of an element.
  - `delete():` Delete the entire linked list.

- Traversal and Querying:
  - `printList():` Return a list of node values.
  - `length():` Return the number of nodes in the list.
  - `getNth(n):` Get the nth node's data.
  - `getNthFromLast(n):` Get the nth node's data from the end.

- Utilities:
  - `isPalindrome():` Check if the list is a palindrome.
  - `checkLoop():` Check for loops in the list.
  - `lengthOfLoop():` Find the length of a loop if it exists.
  - `uniqueSorted():` Retrieve unique elements in sorted order.

- Modify List:
  - `reverseList():` Reverse the order of nodes.
  - `segregateEvenOdd():` Separate even and odd nodes.

- Merging Lists:
  - `mergeTwoLists(l1, l2):` Merge two sorted linked lists.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License.

<img width="1407" alt="image" src="https://github.com/user-attachments/assets/e66a4dfa-ea83-44d0-bbbc-0d2e5fc44d36">

