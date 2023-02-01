def decorate(func):
    print('invoke decorate')
    return func

@decorate
def target():
    print('running target()')

target()

print('\n================================================================\n')


registry = []
def register(func):
    print(f'running register({func}')
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')
    
@register
def f2():
    print('running f2()')
    
def f3():
    print('running f3()')
    
def main():
    print('running main()')
    print('registry main()')
    f1()
    f2()
    f3()
    print('regisry =================================================================')
    print(registry)
    
if __name__ == '__main__':
    main()
