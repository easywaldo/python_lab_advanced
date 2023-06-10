with open('./fluent_python/ch18/mirror.py') as fp:
    src = fp.read(60)
    
print(len(src))
print(fp)
print(fp.closed, fp.encoding)

# can't read more text from fp because at the end of the with block

fp.read(60)