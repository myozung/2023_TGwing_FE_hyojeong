# 1번
def sum(a, b):
    return a+b

# 2번
def sub(a, b):    
    return a-b

# 3번
def mul(a, b):
    return a*b

# 4번
def div(a, b):
    return a/b

# 5번
def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**1/2

# 6번
def title():
    lylics = "Switch sides and I'm beside you."
    return lylics[21:31]

# 7번
def reverseStr(string):
    return string[::-1]

# 8번
def introduce():
    name=input("이름을 입력하세요:")
    
    hobby=input("취미를 입력하세요:")
   
    school=input("재학 중인 학교를 입력하세요:")
   
    birthday=input("생일을 입력하세요:")
    print("제 이름은 %s입니다. 취미는 %s입니다. 저는%s를 다니고 있습니다. 제 생일은 %s월 %s일 입니다."%(name,hobby,school,birthday[2:4],birthday[4:7]))

# 9번
def calc():
    return 