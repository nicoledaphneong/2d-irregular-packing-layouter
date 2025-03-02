from PIL import Image
import numpy as np

class ImagePacker:
    def __init__(self, canvas_width=1080, canvas_height=1920):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    def pack_images(self, images):
        canvases = []
        current_canvas = Image.new('RGBA', (self.canvas_width, self.canvas_height), (255, 255, 255, 0))
        current_canvas_mask = np.zeros((self.canvas_height, self.canvas_width), dtype=bool)

        for image in images:
            placed = False
            for rotation in [0, 90, 180, 270]:
                rotated_image = image.rotate(rotation, expand=True)
                img_width, img_height = rotated_image.size
                img_mask = np.array(rotated_image)[:, :, 3] > 0  # Alpha channel mask

                for y in range(self.canvas_height - img_height + 1):
                    for x in range(self.canvas_width - img_width + 1):
                        if not np.any(current_canvas_mask[y:y+img_height, x:x+img_width] & img_mask):
                            current_canvas.paste(rotated_image, (x, y), rotated_image)
                            current_canvas_mask[y:y+img_height, x:x+img_width] |= img_mask
                            placed = True
                            break
                    if placed:
                        break
                if placed:
                    break

            if not placed:
                canvases.append(current_canvas)
                current_canvas = Image.new('RGBA', (self.canvas_width, self.canvas_height), (255, 255, 255, 0))
                current_canvas_mask = np.zeros((self.canvas_height, self.canvas_width), dtype=bool)
                current_canvas.paste(image, (0, 0), image)
                current_canvas_mask[:img_height, :img_width] = img_mask

        canvases.append(current_canvas)
        return canvases