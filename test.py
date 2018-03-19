class A:
    a = 1
class B:
    a = 3
class C:
    a = 2

aa = A()
bb = B()
cc = C()
l = [aa,bb,cc]
l.sort(key=lambda gen:gen.a)
print (l)
