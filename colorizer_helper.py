from colorizer import load_image, Colorizer#, Decoder
import os
import matplotlib.pyplot as plt
import random



IMAGE_DIR = ".\\test_images\\color"
GS_IMAGE_DIR = ".\\test_images\\grayscale"
IMAGE_PATHS = [os.path.join(IMAGE_DIR, image_path) for image_path in os.listdir(IMAGE_DIR)]
GS_IMAGE_PATHS = [os.path.join(GS_IMAGE_DIR, gs_image_path) for gs_image_path in os.listdir(GS_IMAGE_DIR)]

col = Colorizer()

#7309


def get_number_of_images():
    return len(IMAGE_PATHS)


def get_image(image_number: int):
    return load_image(IMAGE_PATHS[image_number])


def get_gs_image(image_number: int):
    return load_image(GS_IMAGE_PATHS[image_number])


def display_images(image_list: list, rows: int = 1, cols: int = 1, titles: list = []):
    """
    Displays a list of images in a grid.

    :param image_list: List of images.
    :param rows: Number of rows the grid should have.
    :param cols: Number of columns the grid should have.
    :param titles: List of titles for the images.
    """

    max_images = rows * cols
    i = 0
    plt.figure()

    for image in image_list:
        if i >= max_images:
            break
        i = i+1
        plt.subplot(rows, cols, i)
        plt.axis("off")
        plt.imshow(image)
        if len(titles) >= i:
            plt.title(titles[i-1])


def compare(image_id = None):
    """
    Renders the image in greyscale, the colorized image and the original image next to each other.

    :param image_id: Number of the chosen image, must be in range of the number of images. If no number is passed, chooses a random one.
    """
    if image_id == None or image_id > len(IMAGE_PATHS) - 1 or image_id < 0:
        image_id = random.randint(0, get_number_of_images() - 1)
    colorized_image = col.colorize(IMAGE_PATHS[image_id])
    return display_images([get_gs_image(image_id), colorized_image, get_image(image_id)], 1, 3, [f"Input (ID: {image_id})", "Output", "Original"])


def generate_examples(rows: int = 3, cols: int = 5):
    """
    Renders a grid of colorized images

    :param rows: Number of rows the grid should have.
    :param cols: Number of columns the grid should have.
    """
    colorized_examples = []
    example_ids = []

    for i in range(rows * cols):
        image_id = random.randint(0, get_number_of_images() - 1)
        if not any([image_id == id for id in example_ids]):
            example_ids.append(f"ID: {image_id}")
            colorized_image = col.colorize(IMAGE_PATHS[image_id])
            colorized_examples.append(colorized_image)

    return display_images(colorized_examples, rows, cols, example_ids)
