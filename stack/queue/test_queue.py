from stack.queue.my_queue import MyQueue


def test_myqueue():
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    re = queue.pop()
    assert re == 1
    queue.push(5)
    re = queue.pop()
    assert re == 2
    re = queue.pop()
    assert re == 3
    re = queue.pop()
    assert re == 4
    re = queue.pop()
    assert re == 5

    queue.push(1)
    queue.push(2)
    re = queue.peek()
    assert re == 1
    re = queue.pop()
    assert re == 1
    re = queue.empty()
    assert re is False
