def my_generator():
    while True:
        received_value = yield
        print("Received value:", received_value)
        
gen = my_generator()
next(gen)

gen.send(10)
gen.send("Hello")

