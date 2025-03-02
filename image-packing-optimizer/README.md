# Image Packing Optimizer

This project is designed to optimize the packing of 2D PNG images onto a canvas of size 2480 x 3508 pixels using an irregular packing algorithm. The goal is to efficiently utilize the available space while minimizing wasted areas.

## Project Structure

```
image-packing-optimizer
├── src
│   ├── main.py          # Entry point of the application
│   ├── optimizer.py     # Contains the ImageOptimizer class for optimizing images
│   ├── packer.py        # Implements the ImagePacker class for packing images
│   └── utils.py         # Utility functions for loading and saving images
├── requirements.txt      # Lists the dependencies required for the project
└── README.md             # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/image-packing-optimizer.git
   cd image-packing-optimizer
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command in your terminal:

```
python src/main.py
```

You will be prompted to input the paths of the PNG images you wish to pack. The application will then process the images and output the optimized layout in PNG format.

## Algorithms Used

- **Irregular Packing Algorithm**: This algorithm is designed to fit irregularly shaped images into a defined area, minimizing the empty space left after packing. The implementation is handled in the `ImagePacker` class.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.