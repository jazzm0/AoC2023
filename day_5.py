import time
from bisect import bisect_left
from typing import List

seeds = []

seed_soil = {}
ss_keys = []

soil_fertilizer = {}
sf_keys = []

fertilizer_water = {}
fw_keys = []

water_light = {}
wl_keys = []

light_temperature = {}
lt_keys = []

temperature_humidity = {}
th_keys = []

humidity_location = {}
hl_keys = []

ss, sf, fw, wl, lt, th, hl = False, False, False, False, False, False, False


def binary_search(keys: List[int], value: int) -> int:
    return bisect_left(keys, value, 0, len(keys))


def add_entry(s: str, map: dict, keys: List[int]):
    if not s[0].isdigit():
        return
    boundaries = s.split()
    source = int(boundaries[1])
    destination = int(boundaries[0])
    offset = int(boundaries[2]) - 1
    map[source] = (offset, destination)
    keys.append(source)


def map_value(map: dict, keys: List[int], value: int) -> int:
    possible_keys = []
    index = binary_search(keys, value)

    if 0 <= index < len(keys):
        possible_keys.append(keys[index])
    if index > 0:
        possible_keys.append(keys[index - 1])
    if index < len(keys) - 1:
        possible_keys.append(keys[index + 1])

    for key in possible_keys:
        v = map[key]
        if key <= value <= key + v[0]:
            return value - key + v[1]
    return value


with open('day_5.txt') as ifile:
    for line in ifile:
        if line.find("seeds") >= 0:
            for seed in line.split(":")[1].split():
                if seed != "":
                    seeds.append(int(seed.strip()))
        elif line.find("seed-to-soil") >= 0:
            ss = True
        elif line.find("soil-to-fertilizer") >= 0:
            sf = True
        elif line.find("fertilizer-to-water") >= 0:
            fw = True
        elif line.find("water-to-light") >= 0:
            wl = True
        elif line.find("light-to-temperature") >= 0:
            lt = True
        elif line.find("temperature-to-humidity") >= 0:
            th = True
        elif line.find("humidity-to-location") >= 0:
            hl = True

        if hl:
            add_entry(line, humidity_location, hl_keys)
        elif th:
            add_entry(line, temperature_humidity, th_keys)
        elif lt:
            add_entry(line, light_temperature, lt_keys)
        elif wl:
            add_entry(line, water_light, wl_keys)
        elif fw:
            add_entry(line, fertilizer_water, fw_keys)
        elif sf:
            add_entry(line, soil_fertilizer, sf_keys)
        elif ss:
            add_entry(line, seed_soil, ss_keys)

locations = []
ss_keys = sorted(ss_keys)
sf_keys = sorted(sf_keys)
fw_keys = sorted(fw_keys)
wl_keys = sorted(wl_keys)
lt_keys = sorted(lt_keys)
th_keys = sorted(th_keys)
hl_keys = sorted(hl_keys)

for seed in seeds:
    soil = map_value(seed_soil, ss_keys, seed)
    fertilizer = map_value(soil_fertilizer, sf_keys, soil)
    water = map_value(fertilizer_water, fw_keys, fertilizer)
    light = map_value(water_light, wl_keys, water)
    temperature = map_value(light_temperature, lt_keys, light)
    humidity = map_value(temperature_humidity, th_keys, temperature)
    location = map_value(humidity_location, hl_keys, humidity)
    locations.append(location)

print(sorted(locations))
min_location = None
solutions_tried = 0  # 1624044411 roughly 1.6 * 10^9 solutions correct answer is 136096660
started = time.time()

for start in range(0, len(seeds), 2):
    for seed in range(seeds[start], seeds[start] + seeds[start + 1]):
        solutions_tried += 1
        soil = map_value(seed_soil, ss_keys, seed)
        fertilizer = map_value(soil_fertilizer, sf_keys, soil)
        water = map_value(fertilizer_water, fw_keys, fertilizer)
        light = map_value(water_light, wl_keys, water)
        temperature = map_value(light_temperature, lt_keys, light)
        humidity = map_value(temperature_humidity, th_keys, temperature)
        location = map_value(humidity_location, hl_keys, humidity)
        if min_location is None or min_location > location:
            min_location = location

        if solutions_tried % 10 ** 7 == 0:
            print("solutions tried so far: " + str(solutions_tried) + " ,took " +
                  str(time.time() - started) + " seconds")

print(min_location)
