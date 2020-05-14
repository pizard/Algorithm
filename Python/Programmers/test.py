from Programmers.Dynamic_Programming import Q43104_Tile

# N = 1
# print(Q43104_Tile.solution(N))



class Foo():
    def func1(self):
        print("function 1")
    def func2(self):
        print(id(self))


f = Foo()

print("class id : ", id(f))
f.func2()

Foo.func2(f)

a = filter(lambda x : x<10, [0,20,30, 5])
type(a)
print(a)
