from my_queue.array_queue import ArrayQueue
from my_queue.linked_queue import LinkedQueue
from my_queue.circular_queue import CircularQueue


def test_array_queue():
    queue = ArrayQueue(4)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    re = queue.dequeue()
    assert re == 1
    queue.enqueue(4)
    queue.enqueue(5)
    re = queue.enqueue(6)
    assert re is False
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() == 5
    re = queue.dequeue()
    assert re is None


def test_linked_queue():
    queue = LinkedQueue(4)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    re = queue.dequeue()
    assert re == 1
    queue.enqueue(4)
    queue.enqueue(5)
    re = queue.enqueue(6)
    assert re is False
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() == 5
    re = queue.dequeue()
    assert re is None


def test_circular_queue():
    queue = CircularQueue(4)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    re = queue.dequeue()
    assert re == 1
    queue.enqueue(4)
    queue.enqueue(5)
    assert queue.enqueue(5) is False
    re = queue.enqueue(6)
    assert re is False
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.dequeue() is None
    re = queue.dequeue()
    assert re is None
