def max_num(a,b,c):
  return max([a,b,c])

print(max_num(1,2,3))
print(max_num(100,50,1))
print(max_num(15,30,2))

def mult_list(lst):
  if len(lst) == 0:
    return 0
  prod = lst[0]

  if len(lst) > 1:
      for i in lst[1:]:
          prod = prod * i

  return prod


print(mult_list([1, 2, 3]))
print(mult_list([]))
print(mult_list([15]))


def rev_string(my_str):
    return my_str[::-1]


print(rev_string(""))
print(rev_string("apple"))
print(rev_string("mt string"))