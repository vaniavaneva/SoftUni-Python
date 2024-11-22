key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_items = {}
obtained_item = None
while True:
    input_line = input()
    materials = input_line.split()
    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material_name = materials[i + 1].lower()
        if material_name in key_materials:
            key_materials[material_name] += quantity
            if key_materials[material_name] >= 250:
                obtained_item = {
                    'shards': "Shadowmourne",
                    'fragments': "Valanyr",
                    'motes': "Dragonwrath"
                }[material_name]
                key_materials[material_name] -= 250
                break
        else:
            junk_items[material_name] = junk_items.get(material_name, 0) + quantity
    if obtained_item:
        break
print(f"{obtained_item} obtained!")
print(f"shards: {key_materials['shards']}")
print(f"fragments: {key_materials['fragments']}")
print(f"motes: {key_materials['motes']}")
for item, quantity in junk_items.items():
    print(f"{item}: {quantity}")