# default arguments
def fun(a, b=5):
    print("a: ", a)
    print("b: ", b)
fun(8)

# Keyword Arguments
def name(fn, ln):
    print(fn, ln)
# without Keyword arguments
name('Sutar', 'Mansi')
# with keyword arguments
name(ln='Sutar', fn='Mansi')


# variable length arguments
def names(*argv):
    for arg in argv:
        print(arg,end=" ")
# variable keyword arguments
def knames(**kwargs):
    for key, value in kwargs.items():
        print("% s == % s" % (key, value))
names('Mansi', 'Priya', 'Riya','Siya')
print()
knames(fn='Mansi', mn='Bhimrao', ln='Sutar')

