from PIL import Image
import os
import itertools
import json
import random

def generate_nfts():
    directory = os.getcwd()
    front_categories = ['eyes', 'hats']
    back_categories = ['backgrounds', 'textures']
    nft_collection_name = 'NFT Project'

    front_images = []
    back_images = []

    for category in front_categories:
        category_images = []
        category_directory = os.path.join(directory, category)
        for file in os.listdir(category_directory):
            if file.endswith('.png'):
                img = Image.open(os.path.join(category_directory, file)).convert('RGBA')
                filename = os.path.splitext(file)[0]  # Get file name without extension
                category_images.append((img, filename))
        front_images.append(category_images)

    for category in back_categories:
        category_images = []
        category_directory = os.path.join(directory, category)
        for file in os.listdir(category_directory):
            if file.endswith('.png'):
                img = Image.open(os.path.join(category_directory, file)).convert('RGBA')
                filename = os.path.splitext(file)[0]  # Get file name without extension
                category_images.append((img, filename))
        back_images.append(category_images)

    front_combinations = list(itertools.product(*front_images))
    back_combinations = list(itertools.product(*back_images))
    all_combinations = list(itertools.product(back_combinations, front_combinations))
    random.shuffle(all_combinations)

    print(f"Generating Collection. {len(all_combinations)} unique combinations.")

    base_layer = Image.open(os.path.join(directory, 'base.png')).convert('RGBA')
    all_metadata = []

    output_directory = os.path.join(directory, 'out')
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for i, (back_combination, front_combination) in enumerate(all_combinations):
        result = Image.new('RGBA', base_layer.size)
        metadata = {
            'name': f'{nft_collection_name} #{i}',
            'description': f'This is {nft_collection_name} {i} of the original set.',
            'edition': 1,
            'image': f'ipfs://NewUriToReplace/{i}.png',
            'attributes': []
        }

        for layer, filename in back_combination:
            result = Image.alpha_composite(result, layer)
            metadata['attributes'].append({
                'trait_type': 'Background',
                'value': filename
            })

        result = Image.alpha_composite(result, base_layer)

        for layer, filename in front_combination:
            result = Image.alpha_composite(result, layer)
            metadata['attributes'].append({
                'trait_type': 'Accessory',
                'value': filename
            })

        result.save(f'{output_directory}\\{i}.png')
        all_metadata.append(metadata)

    with open(f'{output_directory}\\_metadata.json', 'w') as f:
        json.dump(all_metadata, f, indent=4)

if __name__ == "__main__":
    generate_nfts()
