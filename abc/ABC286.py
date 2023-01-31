def probA():
    N,P,Q,R,S=map(int, input().split())
    A=list(map(int, input().split()))
    
    B=A[:P-1]+A[R-1:S]+A[Q:R-1]+A[P-1:Q]+A[S:]
    print(*B)

def probB():
    N=int(input())
    S=str(input())
    print(S.replace('na', 'nya'))

def main():
    N,A,B=map(int, input().split())
    S=str(input())
    
    def checkPalidrome(string):
        if string==string[::-1]:
            return True
        else:
            return False
    
    

if __name__ == '__main__':
    main()