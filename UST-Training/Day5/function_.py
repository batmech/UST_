import time
# Co-routine Topic
def searcher():
    details = "Hello I am Anido/ I am python programmer. I love coding!"
    time.sleep(1)
    while True:
        text = yield 
        if text in details:
            print(f'Yes, {text} in deatils')
        else: 
            print(f'No, {text} not in details')

search = searcher()
next(search)
search.send('python')
user_input = input('Enter your keywords: ')
search.send(user_input)
user_input = input('Enter your keywords: ')
search.send(user_input)
search.close()