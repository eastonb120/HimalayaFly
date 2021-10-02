import threading

f1_ist = [3,4,5,6]
f2_ist = [6,8,13,12]
def f1(l_ist):
    l_ist.pop()
def f2(l_ist):
    l_ist.pop()


if __name__ == '__main__':
    procs = []
    p1 = Process(target=f1, args=(f1_ist))
    p1.start()
    procs.append(p1)
    p2 = Process(target=f2, args=(f2_ist))
    p2.start()
    procs.append(p2)
    for p in procs:
         p.join()