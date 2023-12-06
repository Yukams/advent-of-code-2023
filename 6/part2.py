from utils.dataReader import read_data

#data = read_data('baseData.txt')
data = read_data('challengeData.txt')
time, distance = [int("".join(line.split(":")[1].strip().split())) for line in data.split("\n")]

res = 0
maxTime = time
for i in range(1, maxTime):
    if(i*(maxTime-i) > distance):
        res+=1

print(res)
