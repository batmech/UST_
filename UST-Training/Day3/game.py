import random

numbers = [i for i in range(1, 9)]
task = [
    'Show phone search history',
    'Do a handstand',
    'do a couple dance',
    'do 20 push-ups',
    'lip reading',
    'story telling',
    'singing a song',
    '15 burpees',
    
]

toDo = {key:val for key,val in zip(numbers, task)}

while len(numbers) >= 0:
    try:
        
        num = random.choice(numbers)
        print('Selected number: ', num)
        print('Selected Task: ', toDo[num])
        numbers.remove(num)
        toDo.pop(num)
    except Exception as e:
        print(e)
        break