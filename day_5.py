seeds = []
seed_soil = {}
soil_fertilizer = {}
fertilizer_water = {}
water_light = {}
light_temperature = {}
temperature_humidity = {}
humidity_location = {}

ss, sf, fw, wl, lt, th, hl = False, False, False, False, False, False, False


def add_entry(s: str, map: dict):
    if not s[0].isdigit():
        return
    boundaries = s.split(" ")
    source = int(boundaries[1])
    destination = int(boundaries[0])
    offset = int(boundaries[2]) - 1
    map[(source, source + offset)] = destination


def map_value(map: dict, value: int) -> int:
    for k, v in map.items():
        if k[0] <= value <= k[1]:
            return value - k[0] + v
    return value


with open('day_5.txt') as ifile:
    for line in ifile:
        if line.find("seeds") >= 0:
            for seed in line.split(":")[1].split(" "):
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
            add_entry(line, humidity_location)
        elif th:
            add_entry(line, temperature_humidity)
        elif lt:
            add_entry(line, light_temperature)
        elif wl:
            add_entry(line, water_light)
        elif fw:
            add_entry(line, fertilizer_water)
        elif sf:
            add_entry(line, soil_fertilizer)
        elif ss:
            add_entry(line, seed_soil)

locations = []

for seed in seeds:
    soil = map_value(seed_soil, seed)
    fertilizer = map_value(soil_fertilizer, soil)
    water = map_value(fertilizer_water, fertilizer)
    light = map_value(water_light, water)
    temperature = map_value(light_temperature, light)
    humidity = map_value(temperature_humidity, temperature)
    location = map_value(humidity_location, humidity)
    locations.append(location)

print(sorted(locations))
