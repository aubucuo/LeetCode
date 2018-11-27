import sys
     
while True:
    try:
        line=sys.stdin.next().strip()
        for i in line:
            if line.count(i)==1:
                print i
                break
    except:
        break