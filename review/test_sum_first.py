from main import sum_first

print("sum_first([1, 2, 3])", sum_first([1, 2, 3]) == 4)
print("sum_first([-1, 2, -3])", sum_first([-1, 2, -3]) == -4)
print("sum_first([1, 2, -3])", sum_first([1, 2, -3]) == -2)
print("sum_first([0, 2, 0])", sum_first([0, 2, 0]) == 0)
print("sum_first([])", sum_first([]) == 0)

print("sum_first(1234)", sum_first(1234) == -1)
print("sum_first('hello')", sum_first('hello') == -1)
print("sum_first(None)", sum_first(None) == -1)
print("sum_first(True)", sum_first(True) == -1)
