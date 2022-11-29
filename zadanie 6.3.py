
def zad3(*args):
    for a in args:
        print(a)

zad3(6, 9, ['zad', 'jfie', 10])

def max(num1, *args):
    m = num1
    for i in args[1:]: #[1:] przejdzie cala liste od pierwszeg oelementu
        if i > m:
            m = i
    return m
print(max(10, 5, 7,-5,4))


