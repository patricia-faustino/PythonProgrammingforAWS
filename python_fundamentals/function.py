""" This script demonstrate the use of Python functions.
The create_shoe function takes a list of materials as input and
determines the type of shoe created based on those materials.
"""


def main():
    # Determine the shoe types based on the materials provided
    materials_1 = ['leather', 'rubber']
    materials_2 = ['grgegre', 'rubber']
    materials_3 = ['mesh', 'rubber']

    # Use the create_shoe function and check the result
    shoe_1 = create_shoe(materials_1)
    shoe_2 = create_shoe(materials_2)
    shoe_3 = create_shoe(materials_3)

    shoes = [shoe_1, shoe_2, shoe_3]
    for shoe in shoes:
        if shoe['type'] == 'unknown':
            print(f"Unknown shoe type for the given materials: {shoe['materials']}")
        else:
            print(f"Shoe created of type: {shoe['type']}")

    print(f"Shoes is of type: {shoe_1['type']}")
    print(f"Shoes is of type: {shoe_2['type']}")
    print(f"Shoes is of type: {shoe_3['type']}")


def create_shoe(materials_list):
    shoe_type = ''

    if 'leather' in materials_list and 'rubber' in materials_list:
        shoe_type = 'boots'
    elif 'mesh' in materials_list and 'rubber' in materials_list:
        shoe_type = 'sneakers'
    else:
        shoe_type = 'unknown'
    return { 'type': shoe_type, 'materials': materials_list}


if __name__ == '__main__':
    main()