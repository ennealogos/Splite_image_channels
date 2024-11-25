# =================================
# the code is based on: https://blog.csdn.net/huanglu_thu13/article/details/52332695
# the original author's github: https://github.com/hlthu
#
# modifications made by me on 2024.11.25
# here is my github: https://github.com/ennealogos
# =================================

import numpy as np
import cv2
import os

def get_red(img):
    red_img = img[:, :, 2]
    return red_img

def get_green(img):
    green_img = img[:, :, 1]
    return green_img

def get_blue(img):
    blue_img = img[:, :, 0]
    return blue_img

def generate_file_path(file_path_old, addition):
    # 分离出文件名
    file_base_name = os.path.basename(file_path_old) # 包括后缀
    file_dir = os.path.dirname(file_path_old) # 文件目录
    file_name, file_ext = os.path.splitext(file_base_name) # 文件名，后缀
    new_path = os.path.join(file_dir, file_name + addition + file_ext)
    return new_path


if __name__ == "__main__":
    file_path = input("please input the path of the file: ")
    img = cv2.imread(file_path)
    if img is None:
        print("Error: Could't load image.")
        exit()

    b, g, r = cv2.split(img)
    # 显示保存前的图像
    cv2.imshow("Blue before", b)
    cv2.imshow("Green before", g)
    cv2.imshow("Red before", r)
    # 分离图像并保存
    b_splited = get_blue(img)
    g_splited = get_green(img)
    r_splited = get_red(img)
    # 显示分离出的单通道图像
    cv2.imshow("Blue after", b_splited)
    cv2.imshow("Green after", g_splited)
    cv2.imshow("Red after", r_splited)
    # 保存
    b_path = generate_file_path(file_path, "_b")
    g_path = generate_file_path(file_path, "_g")
    r_path = generate_file_path(file_path, "_r")
    cv2.imwrite(b_path, b_splited)
    cv2.imwrite(g_path, g_splited)
    cv2.imwrite(r_path, r_splited)
    cv2.waitKey(0)
    cv2.destroyAllWindows()