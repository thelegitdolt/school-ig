from Projects.PA4.fifteen import Fifteen

if __name__ == '__main__':
    a = Fifteen()
    a.update(15)
    for i in a.tiles:
        print(i.id, i.connectedTo)
    while True:

        b = int(input('do the thing fella \n'))
        a.update(b)
        a.draw()
        for i in a.tiles:
            print(i)
        