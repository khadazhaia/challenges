from main import cube

print("cube(5)", cube(5) == 125)
print("cube(2)", cube(2) == 8)
print("cube(0)", cube(0) == 0)
print("cube(-1)", cube(-1) == -1)
print("cube(-5)", cube(-5) == -1)

print("cube('hello')", cube('hello') == -1)
print("cube(None)", cube(None) == -1)
print("cube(True)", cube(True) == -1)
