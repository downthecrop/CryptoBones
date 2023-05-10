# NFT Art Generator

![](./promo.gif)

This project provides a Python script to generate unique NFT (Non-fungible token) art by combining different layers of images. It's especially useful for creating generative art for NFT projects where each piece has a unique combination of traits.

## Features

- Combines different layers of images into unique variants.
- Creates a metadata file for each variant containing information about the traits used.
- Shuffles the combinations to randomize the order of the generated NFTs.
- Stores all metadata in a single JSON file.

## Prerequisites

- Python 3.7 or later.
- The Python Imaging Library (PIL). You can install it with pip:

```
pip install pillow
```
Clone this repository.

- Place your layer images in separate folders within a main folder. The script currently expects two types of layers: front layers and back layers.

- Update the nft_collection_name, front_categories, and back_categories variables in the Python script to match your folder structure.

Run the Python script:

```
python nft_art_generator.py
```

The script will generate the unique variants and store them in the specified output folder, along with the metadata JSON file.

Please note that this script is intended to be a starting point and may need to be customized to suit your particular needs.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is open source and available under the MIT License.

