from colorizer import load_image, Colorizer#, Decoder
import os

IMAGE_DIR = ".\\test_images\\color"
GS_IMAGE_DIR = ".\\test_images\\grayscale"
IMAGE_PATHS = [os.path.join(IMAGE_DIR, image_path) for image_path in os.listdir(IMAGE_DIR)]
GS_IMAGE_PATHS = [os.path.join(GS_IMAGE_DIR, gs_image_path) for gs_image_path in os.listdir(GS_IMAGE_DIR)]

col = Colorizer()

loss = col.evaluate_decoder(IMAGE_PATHS[:10])

print(f"EVAL: {loss}")
