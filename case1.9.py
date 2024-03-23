print("Введите плей-лист папы:")
my_str = ''
for i in range(5):
    l = str(input())
    my_str = my_str + l + '\n'
print("\nПлей-лист мамы")
def reversed1(variable):
    res=''
    for i in range(len(variable)-1,-1,-1):
        res+=variable[i]
    return res

n = reversed1(my_str)
print(n)