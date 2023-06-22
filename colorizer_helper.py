import os
import random

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from colorizer import Colorizer, load_image  # , Decoder

BASE_PATH = os.path.relpath(os.path.dirname(__file__))
IMAGE_DIR = os.path.join(BASE_PATH, "test_images/color/")
GS_IMAGE_DIR = os.path.join(BASE_PATH, "test_images/grayscale/")
IMAGE_PATHS = [os.path.join(IMAGE_DIR, image_path) for image_path in os.listdir(IMAGE_DIR)]
GS_IMAGE_PATHS = [os.path.join(GS_IMAGE_DIR, gs_image_path) for gs_image_path in os.listdir(GS_IMAGE_DIR)]
CATEGORIES_PATH = os.path.join(BASE_PATH, "imagenet_kaggle_folders.csv")

@st.cache_resource
def get_colorizer():
    col = Colorizer()
    return col

@st.cache_resource
def get_categories_df():
    df = pd.read_csv(CATEGORIES_PATH)
    return df

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
    image_path = IMAGE_PATHS[image_id]
    category_id = os.path.basename(image_path).split('_')[0]
    colorized_image = get_colorizer().colorize(image_path)
    df = get_categories_df()
    category = df[df.kaggle_folder == category_id]
    if category.empty:
        category_name = "Unknown"
    else:
        category_name = category['class'].values[0]
    return display_images([get_gs_image(image_id), colorized_image, get_image(image_id)], 1, 3, [f"Input (ID: {image_id} {category_name})", "Output", "Original"])


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
            colorized_image = get_colorizer().colorize(IMAGE_PATHS[image_id])
            colorized_examples.append(colorized_image)

    return display_images(colorized_examples, rows, cols, example_ids)
