from utils.dataReader import read_data

#data = read_data('baseData.txt')
#data = read_data('testData.txt')
data = read_data('challengeData.txt')

splitData = data.split("\n")
instructions = [0 if step == 'L' else 1 for step in splitData[0]]
map = {fKey:(v1,v2) for (fKey,(v1, v2)) in
        ((key.strip(), value.strip()[1:-1].split(",")) for (key, value) in (mapping.replace(" ", "").split("=") for mapping in splitData[2:]))
       }

positions = [key for key in map.keys() if key[2] == "A"]

# This code runs potentially for multiple years before finding a solution
"""
count=0
iLen = len(instructions)
while not all([True if position[2] == "Z" else False for position in positions]):
    for idx, position in enumerate(positions):
        positions[idx] = map[position][instructions[count % iLen]]
    count += 1
    print(str(count) + " : " + str(positions))

print(count)
"""
