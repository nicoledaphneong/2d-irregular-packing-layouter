from packer import ImagePacker

class ImageOptimizer:
    def __init__(self, canvas_width=1080, canvas_height=1920):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height

    def optimize_images(self, images):
        packed_images = self.pack_images(images)
        return packed_images

    def pack_images(self, images):
        packer = ImagePacker(self.canvas_width, self.canvas_height)
        return packer.pack_images(images)