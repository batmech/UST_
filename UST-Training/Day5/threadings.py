from concurrent.futures import thread
import time
import threading

def printCubes(num):
    time.sleep(2)
    print(f'Cube of {num}: {num**3}')

def printSquare(num):
    time.sleep(2)
    print(f'Square of {num}: {num*num}')

first = threading.Thread(target=printSquare, args=(10, ))
sec = threading.Thread(target=printCubes, args=(10, ))
first.start()
sec.start()
first.join()
sec.join()
print('Done')