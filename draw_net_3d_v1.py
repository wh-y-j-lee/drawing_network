# Made by YongJu Lee 18.04.09

import cv2
import random
import numpy as np
from builtins import print


def main():
    # 배경 이미지 사이즈 (세로, 가로)
    background_size = (1024,1024)


    # 원하는 사각형 사이즈 (세로, 가로)
    filter_size = (100,100)

    # 메인 윈도우 생성
    main_window = make_rect(background_size)

    # 원하는 사각형 위치 세로, 가로 설정
    center_y = 200
    center_x = 200

    # 사각형 개수
    n = 20

    # 사각형 간격 조절
    interval = 2


    # 원하는 두가지 색 조절 (B, G, R) <= OpenCV라서 BGR순서로 해야합니다.
    rect1 = make_rect(filter_size, (0, 0, 0))
    rect2 = make_rect(filter_size, (75, 75, 75))

    # rect3 이런식으로 추가해도 됨 그러면 아래 배열에도 추가해줘야 한다.
    rect = [rect1, rect2]   #사각형들 리스트화

    # n개의 사각형 배치
    # set_n_rect(main_window, rect, (center_y, center_x), n, interval, forward=True)
    set_3d_rect(main_window,(center_y,center_x),(100,50,100,45), 2 ,(75,75,75),1)
    '''
    랜덤한 Color 사각형으로 하고 싶을 경우
    =======================================================
    '''
    # # 랜덤 두가지 색
    # c1 = random_color()
    # c2 = random_color()
    # # 아래 주석 해제
    #
    # rect_r1 = make_rect(filter_size, c1)
    # rect_r2 = make_rect(filter_size, c2)
    #
    # rect_rand = [rect_r1, rect_r2]
    # set_n_rect(main_window, rect_rand, (center_y, center_x), n, interval)
    #

    cv2.imshow('window',main_window)
    cv2.waitKey(0)

def make_rect(size, color=(255,255,255)):
    width = size[0]
    height = size[1]
    if len(color)== 3:
        out = np.full((width,height,3),color,dtype=np.uint8)
    elif len(color)==1:
        out = np.full((width, height), color, dtype=np.uint8)
    return out
def set_rect(src,rect,points):
    src[points[0]:points[0]+rect.shape[0], points[1]:points[1]+rect.shape[1]] = rect

def set_n_rect(src, rects, center, iter, interval, forward = True ):
    if forward:
        for i in range(0, iter):
            set_rect(src, rects[i%len(rects)], (center[0] + i * interval, center[1] + i * interval))
    else:
        for i in range(0, iter):
            set_rect(src, rects[i%len(rects)], (center[0] + i * interval, center[1] - i * interval))

def set_3d_rect(src, center, size, interval, color = (255,255,255), direction = 1):
    #size(width,height,length,angle)

    '''              '4  '5         '   '
                    '0  '1 '6      '   ''
                    '2  '3         '   '
    '''
    rect = make_rect(size[:2], color)
    width = size[0]
    height = size[1]
    length = size[2]
    if direction == 1:
        angle = size[3]
    elif direction == 2:
        angle = 180 - size[3]
    l_1 = int(length*np.cos(angle / 180 * np.pi))
    l_2 = int(length * np.sin(angle / 180 * np.pi))
    point_0 = center
    point_1 = (center[0]+size[1], center[1])
    point_2 = (center[0], center[1]+size[0])
    point_3 = (center[0]+size[1], center[1]+size[0])
    point_4 = (center[0] + l_1, center[1] - l_2)
    point_5 = (center[0] + l_1 + size[1], center[1] - l_2)
    if direction ==1:
        point_6 = (point_3[0] + l_1, point_3[1] - l_2)
    elif direction ==2:
        point_6 = (point_2[0] + l_1, point_2[1] - l_2)

    # TODO 1: 1st Rect (윗면)
    # if direction == 1:
    cv2.fillConvexPoly(src, np.array((point_0, point_1, point_5, point_4), dtype=int), color)
    # elif direction == 2:
    #     cv2.fillConvexPoly(src, np.array(((point_0[0]-interval,point_0[1]), (point_1[0]-interval,point_1[1]), point_5, point_4), dtype=int), color)
    # TODO 2: 2st Rect (정면)
    if direction ==1:
        set_rect(src, rect, (center[0]+interval,center[1]-interval))
    elif direction==2:
        set_rect(src, rect, (center[0] , center[1] + interval))
    # TODO 3: 3st Rect (옆면)
    if direction ==1:
        cv2.fillConvexPoly(src, np.array(((point_1[0], point_1[1]+interval), point_3, point_6, (point_5[0],point_5[1]+interval)), dtype=int), color)
    elif direction == 2:
        cv2.fillConvexPoly(src, np.array(
            ((point_0[0], point_0[1] + interval), point_2, point_6, (point_4[0], point_4[1] + interval)),
            dtype=int), color)
def random_color(templete = 'Normal', threshold = 75):
    if templete =='Normal':
        color = (random.randint(0,255),random.randint(0,255), random.randint(0,255))
    elif templete == 'blue':
        color = (random.randint(0, 255), random.randint(0, threshold), random.randint(0, threshold))
    elif templete == 'red':
        color = (random.randint(0, threshold), random.randint(0, threshold), random.randint(0, 255))
    elif templete == 'green':
        color = (random.randint(0, threshold), random.randint(0, 255), random.randint(0, threshold))
    elif templete == 'black':
        color = (random.randint(0, threshold), random.randint(0, threshold), random.randint(0, threshold))

    return color

if __name__ == '__main__':
    main()
    # print(random_color())