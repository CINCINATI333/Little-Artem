b = int(input())
a = [[] for k in range(b)]
for k in range(b):
    a[k] = str(input())
    a[k] = a[k].split()

for x in range(b):
    ans = ''
    if int(a[x][0])%2 == 1 and int(a[x][1])%2 == 1:
        for k in range(int(a[x][0])):
            if k%2 == 1:
                for i in range(int(a[x][1])):
                    if k%2 == 1:
                        if i%2 == 1:
                            ans += 'B'
                        else:
                            ans += 'W'
            else:
                for i in range(int(a[x][1])):
                        if i%2 == 1:
                            ans += 'W'
                        else:
                            ans += 'B'
            print(ans)
            ans = ''
    elif int(a[x][0])%2 == 0 and int(a[x][1])%2 == 1 or int(a[x][0])%2 == 1 and int(a[x][1])%2 == 0:
        for k in range(1,int(a[x][0])+1):
            if k < int(a[x][0]):
                if k%2 == 0:
                    for i in range(1,int(a[x][1])+1):
                            if i%2 == 0:
                                ans += 'B'
                            else:
                                ans += 'W'
                elif k%2 == 1:
                    for i in range(1,int(a[x][1])+1):
                            if i%2 == 0:
                                ans += 'W'
                            else:
                                ans += 'B'
            else:
                if k%2 == 0:
                    for i in range(1,int(a[x][1])+1):
                        if i < int(a[x][1]):
                            if i%2 == 0:
                                ans += 'B'
                            else:
                                ans += 'W'

                        else:
                            ans += 'B'
                elif k%2 == 1:
                    for i in range(1,int(a[x][1])+1):
                        if i < int(a[x][1]):
                            if i%2 == 0:
                                ans += 'W'
                            else:
                                ans += 'B'
                        else:
                            ans += 'B'
            print(ans)
            ans = ''
    elif int(a[x][0])%2 == 0 and int(a[x][1])%2 == 0 or int(a[x][0])%2 == 1 and int(a[x][1])%2 == 0:
        for k in range(1,int(a[x][0])+1):
            if k != int(a[x][0]) - 1:
                if k%2 == 0:
                    for i in range(1,int(a[x][1])+1):
                            if i%2 == 0:
                                ans += 'B'
                            else:
                                ans += 'W'
                elif k%2 == 1:
                    for i in range(1,int(a[x][1])+1):
                            if i%2 == 0:
                                ans += 'W'
                            else:
                                ans += 'B'
            else:
                if k%2 == 0:
                    for i in range(1,int(a[x][1])+1):
                        if i < int(a[x][1]):
                            if i%2 == 0:
                                ans += 'B'
                            else:
                                ans += 'W'

                        else:
                            ans += 'B'
                elif k%2 == 1:
                    for i in range(1,int(a[x][1])+1):
                        if i < int(a[x][1]):
                            if i%2 == 0:
                                ans += 'W'
                            else:
                                ans += 'B'
                        else:
                            ans += 'B'
            print(ans)
            ans = ''                                                 
          
