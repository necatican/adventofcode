import os
dir_path = os.path.dirname(os.path.realpath(__file__))
input_file = open(os.path.join(dir_path, "input"), 'r')
lines = input_file.readlines()


def count_bags(bags, target_bag):
    if target_bag not in bags:
        return 1
    bag_count = 1
    contained_bags = bags[target_bag]
    for bag in contained_bags:
        bag_count += int(bag[1]) * count_bags(bags, bag[0])

    return bag_count


bags = {}  # {container: target bag} pair
for line in lines:
    line_parts = line.strip()[:-1].split('contain')  # [:-1] to remove the dots
    container = line_parts[0].strip()[:-1]  # 'x bags' to 'x bag'
    target_bags = line_parts[1].split(',')

    container_bags = []
    for bag in target_bags:
        bag = bag.strip()
        if bag == 'no other bags':
            bags[container] = None
            continue

        bag_name = bag[2:]
        bag_count = bag[:1]
        if bag_name.endswith('bags'):
            bag_name = bag_name[:-1]  # 'x bags' to 'x bag'
        container_bags.append((bag_name, bag_count))
    bags[container] = container_bags

# Count should not include the gold bag
print(count_bags(bags, 'shiny gold bag') - 1)
