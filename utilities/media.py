import os

import cv2


def create_video():
    input_folder = '../graphics/generations/img'
    output_folder = '../graphics/generations/video'
    os.makedirs(output_folder, exist_ok=True)

    file_names = sorted(
        [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.png')])

    output_mp4 = '../graphics/generations/video/generations.mp4'

    img = cv2.imread(file_names[0])
    height, width, _ = img.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_mp4, fourcc, 15, (width, height))

    for file in file_names:
        img = cv2.imread(file)
        video.write(img)

    video.release()

    print(f'MP4 saved: {output_mp4}')
