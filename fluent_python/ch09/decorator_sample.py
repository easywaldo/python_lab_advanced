def decorate(func):
    print('invoke decorate')
    return func

@decorate
def target():
    print('running target()')

target()
