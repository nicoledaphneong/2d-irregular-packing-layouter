import os
from tkinter import Tk, filedialog
from optimizer import ImageOptimizer
from utils import load_image, save_image

def main():
    root = Tk()
    root.withdraw()  # Hide the root window

    input_images = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )

    if not input_images:
        print("No images selected. Exiting.")
        return

    optimizer = ImageOptimizer()
    loaded_images = [load_image(img_path) for img_path in input_images]
    optimized_layouts = optimizer.optimize_images(loaded_images)

    for i, layout in enumerate(optimized_layouts):
        output_path = f"packed_output_{i + 1}.png"
        save_image(layout, output_path)
        print(f"Packed image saved as {output_path}")

if __name__ == "__main__":
    main()