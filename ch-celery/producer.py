import tasks

# tasks.add.delay(2, 2)


result = tasks.add.delay(3, 9)

print('get result')

print(result.get())