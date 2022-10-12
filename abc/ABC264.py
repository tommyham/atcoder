def probA():
    L,R=map(int, input().split())
    string="atcoder"
    print(string[L-1:R])

def probB():
    R,C=map(int, input().split())
    
    def search(R,C):
        string=""
        if not (R-1)%2:
            if abs(C-8)<=abs(R-8):
                string="black"
            else:
                if abs(C-8)%2:
                    string="black"
                else:
                    string="white"
        else:
            if abs(C-8)<=abs(R-8):
                string="white"
            else:
                if abs(C-8)%2:
                    string="black"
                else:
                    string="white"
        return string
    print(search(R, C))

# H1,W1=map(int, input().split())
# A=[list(map(int, input().split())) for _ in range(H1)]
# H2,W2=map(int, input().split())
# B=[list(map(int, input().split())) for _ in range(H2)]

H1,W1=4,5
H2,W2=2,3
A=[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
B=[[6, 8, 9], [16, 18, 19]]

def compare(array1,array2):
    for i in range(len(array1)):
        for j in range(len(array1[i])):
            if array1[i][j]!=array2[i][j]:
                return False
    
    return True
