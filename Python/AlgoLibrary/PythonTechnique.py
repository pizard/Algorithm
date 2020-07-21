# Deep Copy
#   _ex = ex[:]
# value 확인
#   op = [x for x in ['*', '+', '-'] if x in expression]
#   {i : [] for i in range(n)}
# return permutation to list
#   op = [list(y) for y in permutations(op)]

# 무한대의 값 : float('inf') or float('-inf')
#   min(\dict.get(\key1, float('inf')), \dict.get(\key2, float('inf')))
#       ->  dict에 해당 key 값이 없는경우 최대 값을 반환