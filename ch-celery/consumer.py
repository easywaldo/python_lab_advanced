import tasks

result = tasks.add.delay(3, 9)

print('get result')

print(result.get())