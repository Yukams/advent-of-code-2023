from utils.dataReader import read_data

#data = read_data('baseData.txt')
data = read_data('challengeData.txt')

splitData = data.split("\n")
instructions = [0 if step == 'L' else 1 for step in splitData[0]]
map = {fKey:(v1,v2) for (fKey,(v1, v2)) in
        ((key.strip(), value.strip()[1:-1].split(",")) for (key, value) in (mapping.replace(" ", "").split("=") for mapping in splitData[2:]))
       }

position = "AAA"
count=0
iLen = len(instructions)
while(position != "ZZZ"):
    position = map[position][instructions[count % iLen]]
    count += 1

print(count)
