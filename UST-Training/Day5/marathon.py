import random
import threading

LIMIT = 1_000_000
startEvent = threading.Event()

class Person:
    def __init__(self, name):
        self.track = 0
        self.name = name
        self.speed = random.randint(10, 15)

def marathon(other):
    if isinstance(other, Person):
        startEvent.wait()
        while other.track < LIMIT:
            other.track += other.speed
        
        print(f'{other.name} completed the race!')

names = ['Allwyn', 'Nibu', 'James Bond', 'Peekcock', 'Lakshman']
participants = [Person(name) for name in names]
threads = [threading.Thread(target=marathon, args=(participant,)) for participant in participants]

for thread in threads:
    thread.start()

startEvent.set()

for thread in threads:
    thread.join()

print('Done!!')

participants.sort(key=lambda x: x.track, reverse=True)
results = [f"{participant.name} completed the race!" 
           for participant in participants
        ]
Content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Marathon Results</title>
    <style>
        *{{
            margin: 0px;
            padding: 0 px;
        }}
        .container{{
            width: 100%;
            height: 100%;
            display: flex;
            background-color: blueviolet;
        }}
        .square{{
            width: 200px;
            color: white;
            margin: 20px;
            height: 200px;
            display: flex;
            align-items: center;
            justify-items: center;
            background-color: green;
        }}
    </style>
</head>
<body>
    <div class="container">
        {''.join(f'<div class="square"><p>{result}</p></div>' for result in results)}
    </div>
</body>
</html>
"""

with open('marathon.html', 'w') as fp:
    fp.write(Content)
