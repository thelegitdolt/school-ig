from Projects.PA3.stack import Stack

# a driver program for class Stack

if __name__ == '__main__':

    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)

    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
