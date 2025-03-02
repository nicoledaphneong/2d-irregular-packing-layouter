from PIL import Image

def load_image(file_path):
    return Image.open(file_path)

def save_image(image, file_path, dpi):
    image.save(file_path, format='PNG', dpi=(dpi, dpi))