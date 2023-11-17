import os

base_path = 'image_tagger_crawled_data'

names = [
    'clothing_store.json',
    'hotel_lobby.json',
    'outdoor_garden.json',
    'wine_cellar.json',
    'game_room.json',
    'kids_room.json',
    'outdoor_patio.json',
    'garage.json',
    'laundry_room.json',
    'outdoor_pool.json',
    'home_gym.json',
    'office.json',
    'walk_in_closet.json',
]
for name in names:
    json_file = os.path.join(base_path, name)
    # print(json_file)
    with open(json_file, 'r') as f:
        data = f.read()
    data = data.replace('][', ',')

    with open(json_file, 'w') as f:
        f.write(data)
    print(f"{json_file} \t ======> \t Done")
