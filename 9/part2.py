from utils.dataReader import read_data

#data = read_data('baseData.txt')
data = read_data('challengeData.txt')

history_data = [[int(elem) for elem in line.split(" ")] for line in data.split("\n")]
sum=0
for history in history_data:
    sub_histories = [history]

    # while all data in a history line is not 0
    while not sub_histories[-1].count(0) == len(sub_histories[-1]):
        sub_history = []

        for i in range(len(sub_histories[-1])-1):
            sub_history.append(sub_histories[-1][i+1] - sub_histories[-1][i])

        sub_histories.append(sub_history)

    # calculate before first history value
    sub_histories[-1].insert(0, 0)
    for i in range(1, len(sub_histories)):
        sub_histories[-(i+1)].insert(0, sub_histories[-(i+1)][0] - sub_histories[-i][0])
    sum += sub_histories[0][0]

print(sum)