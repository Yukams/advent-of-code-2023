from utils.dataReader import read_data

"""
Converts :
[[0,15,3],
[5,6,2]]

To :
{0:15, 1:16, 2:17, 5:6, 6:7}
"""
def generate_map(list_as_string):
    data_list = generate_list(list_as_string)
    dic = {}
    for key_list in data_list:
        for i in range(key_list[2]):
            dic[key_list[1] + i] = key_list[0] + i
    return dic


"""
Converts :
"0 15 37
37 52 2
39 0 15"

To :
[[0,15,37],
[37,52,2],
[39,0,15]]
"""
def generate_list(list_as_string):
    return [[int(num_string) for num_string in string_list.split(" ")] for string_list in list_as_string.split("\n")]


"""
fv=Find Value
Finds the value of the key in the dictionary, else return itself
"""
def fv(dic, key):
    return key if key not in dic else dic[key]


def apply_mapping(mapping, items):
    map_result = generate_map(mapping)
    for idx, item in enumerate(items):
        items[idx] = fv(map_result, item)
    return items


#data = read_data('baseData.txt')
data = read_data('challengeData.txt')
(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature,
 temperature_to_humidity, humidity_to_location) = \
    [data_string.split(":")[1].strip() for data_string in data.split("\n\n")]

seeds = generate_list(seeds)[0]

seeds = apply_mapping(seed_to_soil, seeds)
print("Step 1 : Done")
seeds = apply_mapping(soil_to_fertilizer, seeds)
print("Step 2 : Done")
seeds = apply_mapping(fertilizer_to_water, seeds)
print("Step 3 : Done")
seeds = apply_mapping(water_to_light, seeds)
print("Step 4 : Done")
seeds = apply_mapping(light_to_temperature, seeds)
print("Step 5 : Done")
seeds = apply_mapping(temperature_to_humidity, seeds)
print("Step 6 : Done")
seeds = apply_mapping(humidity_to_location, seeds)
print("Step 7 : Done")

print(min(seeds))
