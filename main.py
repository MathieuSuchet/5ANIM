import cv2
import numpy as np
import os

def create_animation(picture_number):
    directory = "animations"
    
    if not os.path.exists(os.path.join(os.getcwd(), directory)):
        os.mkdir(os.path.join(os.getcwd(), directory))
    
    # Charger les images réelle et générée
    real_image = cv2.imread("pytorch-CycleGAN-and-pix2pix\\results\\facades_label2photo_pretrained\\test_latest\\images\\" + str(picture_number) + "_real_B.png")
    generated_image = cv2.imread("pytorch-CycleGAN-and-pix2pix\\results\\facades_label2photo_pretrained\\test_latest\\images\\" + str(picture_number) + "_fake_B.png")

    # S'assurer que les tailles sont identiques
    assert real_image.shape == generated_image.shape, "Les images doivent avoir les mêmes dimensions."

    # Générer les images intermédiaires
    frames = []
    steps = 90  # Nombre d'images intermédiaires
    for i in range(steps + 1):
        alpha = i / steps
        intermediate = cv2.addWeighted(real_image, 1 - alpha, generated_image, alpha, 0)
        frames.append(intermediate)

    # Sauvegarder une animation en vidéo ou GIF
    output = directory + "/animation_" + str(picture_number) + ".mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    height, width, _ = real_image.shape
    video_writer = cv2.VideoWriter(output, fourcc, 30, (width, height))

    for frame in frames:
        video_writer.write(frame)
    video_writer.release()

    print("Animation générée avec succès :", output)
    
for i in range(10, 48):
    create_animation(i)