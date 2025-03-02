import os
from tkinter import Tk, filedialog, messagebox, Label, Entry, OptionMenu, StringVar, IntVar, Button, PhotoImage
from optimizer import ImageOptimizer
from utils import load_image, save_image

def convert_to_pixels(value, unit, dpi):
    if unit == "inches":
        return value * dpi
    elif unit == "cm":
        return value * dpi / 2.54
    elif unit == "mm":
        return value * dpi / 25.4
    return value

def convert_from_pixels(value, unit, dpi):
    if unit == "inches":
        return value / dpi
    elif unit == "cm":
        return value * 2.54 / dpi
    elif unit == "mm":
        return value * 25.4 / dpi
    return value

def update_dimensions(*args):
    global current_unit
    try:
        width = float(width_var.get())
        height = float(height_var.get())
        dpi = int(dpi_var.get())
        unit = unit_var.get()

        width_px = convert_to_pixels(width, current_unit, dpi)
        height_px = convert_to_pixels(height, current_unit, dpi)

        if unit == "inches":
            width_var.set(f"{convert_from_pixels(width_px, 'inches', dpi):.2f}")
            height_var.set(f"{convert_from_pixels(height_px, 'inches', dpi):.2f}")
        elif unit == "cm":
            width_var.set(f"{convert_from_pixels(width_px, 'cm', dpi):.2f}")
            height_var.set(f"{convert_from_pixels(height_px, 'cm', dpi):.2f}")
        elif unit == "mm":
            width_var.set(f"{convert_from_pixels(width_px, 'mm', dpi):.2f}")
            height_var.set(f"{convert_from_pixels(height_px, 'mm', dpi):.2f}")
        else:
            width_var.set(f"{width_px:.0f}")
            height_var.set(f"{height_px:.0f}")

        current_unit = unit
    except ValueError:
        pass

def show_image(index):
    global image_label, quantity_var, images, image_paths

    if 0 <= index < len(images):
        image = images[index]
        photo = PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo
        quantity_var.set(quantities[index])
        current_image_index.set(index)

def next_image():
    index = current_image_index.get() + 1
    if index < len(images):
        show_image(index)

def previous_image():
    index = current_image_index.get() - 1
    if index >= 0:
        show_image(index)

def update_quantity(*args):
    index = current_image_index.get()
    quantities[index] = int(quantity_var.get())

def get_canvas_dimensions():
    root = Tk()
    root.title("Canvas Dimensions")

    global width_var, height_var, unit_var, dpi_var, current_unit, images, image_paths, quantities, current_image_index, image_label, quantity_var

    width_var = StringVar(value="1")
    height_var = StringVar(value="1")
    unit_var = StringVar(value="inches")
    dpi_var = IntVar(value=300)
    current_unit = "inches"
    images = []
    image_paths = []
    quantities = []
    current_image_index = IntVar(value=0)

    Label(root, text="Width:").grid(row=0, column=0)
    width_entry = Entry(root, textvariable=width_var)
    width_entry.grid(row=0, column=1)
    Label(root, text="Height:").grid(row=1, column=0)
    height_entry = Entry(root, textvariable=height_var)
    height_entry.grid(row=1, column=1)
    Label(root, text="Unit:").grid(row=2, column=0)
    unit_menu = OptionMenu(root, unit_var, "pixels", "inches", "cm", "mm")
    unit_menu.grid(row=2, column=1)
    Label(root, text="DPI:").grid(row=3, column=0)
    dpi_entry = Entry(root, textvariable=dpi_var)
    dpi_entry.grid(row=3, column=1)

    Button(root, text="Select Images", command=select_images).grid(row=4, column=0, columnspan=2)

    image_label = Label(root)
    image_label.grid(row=5, column=0, columnspan=2)

    quantity_var = IntVar(value=1)
    quantity_var.trace("w", update_quantity)
    Label(root, text="Quantity:").grid(row=6, column=0)
    Entry(root, textvariable=quantity_var).grid(row=6, column=1)

    Button(root, text="Previous", command=previous_image).grid(row=7, column=0)
    Button(root, text="Next", command=next_image).grid(row=7, column=1)

    unit_var.trace("w", update_dimensions)
    width_entry.bind("<FocusOut>", update_dimensions)
    height_entry.bind("<FocusOut>", update_dimensions)
    dpi_entry.bind("<FocusOut>", update_dimensions)

    root.mainloop()

    width = float(width_var.get())
    height = float(height_var.get())
    dpi = int(dpi_var.get())
    unit = unit_var.get()

    width_px = convert_to_pixels(width, unit, dpi)
    height_px = convert_to_pixels(height, unit, dpi)

    root.destroy()
    return int(width_px), int(height_px), dpi

def select_images():
    global images, image_paths, quantities

    image_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
    )

    if not image_paths:
        messagebox.showerror("Error", "No images selected.")
        return

    images = [load_image(img_path) for img_path in image_paths]
    quantities = [1] * len(images)

    show_image(0)

def main():
    canvas_dimensions = get_canvas_dimensions()
    if not canvas_dimensions:
        return

    canvas_width, canvas_height, dpi = canvas_dimensions
    optimizer = ImageOptimizer(canvas_width, canvas_height)

    loaded_images = []
    for img_path, quantity in zip(image_paths, quantities):
        image = load_image(img_path)
        loaded_images.extend([image] * quantity)

    optimized_layouts = optimizer.optimize_images(loaded_images)

    for i, layout in enumerate(optimized_layouts):
        output_path = f"packed_output_{i + 1}.png"
        save_image(layout, output_path, dpi)
        print(f"Packed image saved as {output_path}")

if __name__ == "__main__":
    main()