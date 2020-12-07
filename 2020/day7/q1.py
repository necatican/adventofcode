import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()


def bag_possibilities(bags, target_bag):
    if target_bag not in bags:
        return []
    possibilities = set()
    possibilities.update(bags[target_bag])
    for possibility in possibilities.copy():
        possibilities.update(bag_possibilities(bags, possibility))

    return possibilities


bags = {}  # {target bag : container} pair
for line in lines:
    line_parts = line.strip()[:-1].split('contain')  # [:-1] to remove the dots
    container = line_parts[0].strip()[:-1]  # 'x bags' to 'x bag'
    target_bags = line_parts[1].split(',')
    for bag in target_bags:
        bag = bag.strip()
        if bag == 'no other bags':
            if 'none' not in bags:
                bags['none'] = []
            bags['none'].append(container)
        else:
            bag_name = bag[2:]
            if bag_name.endswith('bags'):
                bag_name = bag_name[:-1]  # 'x bags' to 'x bag'
            if bag_name not in bags:
                bags[bag_name] = []
            bags[bag_name].append(container)

print(len(bag_possibilities(bags, 'shiny gold bag')))
