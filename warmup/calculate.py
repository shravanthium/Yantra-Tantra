from collections import Counter
import sys
import math

def mean(num):
    mean = sum(num)/len(num)
    return mean

def median(num): 
    mid = len(num)/2
    if len(num)%2==0:
        median = (num[mid]+num[mid-1])/2
    else:
        median = num[mid]
    return median
    
def mode(num):
    mode = num[0]
    if mode - int(mode)==0:
        return int(mode)
    else:
        return mode 

def sd(num):
    m=mean(num)
    sum=0
    for i in num:
        sum += (i-m)*(i-m)
    c=sum/len(num)
    return round(math.sqrt(c),1)
    
def ci(num):
    m = mean(num)
    d = sd(num)
    x = 1.96*(d/math.sqrt(len(num)))
    return x

def main():
    num = ""
    for line in sys.stdin:
        num += line
    num = num.split('\n')
    l=[]
    for i in num[1:]:
        l.extend(i.split(' '))
    num = []
    num = [ float(i) for i in l]
    print mean(num),'\n',median(sorted(num)),'\n',mode(sorted(num)),'\n',sd(sorted(num)),'\n',round(mean(sorted(num))-     ci(sorted(num)),1),round(mean(sorted(num))+ci(sorted(num)),1)

if __name__ == "__main__":
    main()

