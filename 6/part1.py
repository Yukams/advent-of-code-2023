from utils.dataReader import read_data

#data = read_data('baseData.txt')
data = read_data('challengeData.txt')
time, distance = [list(map(int, line.split(":")[1].strip().split())) for line in data.split("\n")]

res = 0
for idxRace in range(len(time)):
    maxTime = time[idxRace]
    tmpRes = 0
    for i in range(1, maxTime):
        if(i*(maxTime-i) > distance[idxRace]):
            tmpRes+=1

    res = tmpRes if res == 0 else tmpRes*res

print(res)
