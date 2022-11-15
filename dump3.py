#bubble sort is used for the leaderboard :)
data=[['a',33,100],['b',39,99],['c',39,100],['d',22,100]]
n = len(data)
for i in range(n):
    for j in range(0,n-i-1):
        
        if data[j][1] > data[j+1][1]:
            data[j],data[j+1] = data[j+1],data[j]
        if data[j][1] == data[j+1][1] and data[j][2] > data[j+1][2]:
            data[j],data[j+1] = data[j+1],data[j]

print(data)
