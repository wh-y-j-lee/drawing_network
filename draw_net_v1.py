# Made by YongJu Lee 18.04.09
# Version 1
'''
=====================================
| YongJu Lee, M.S. Student
| IMAGE AND VIDEO PATTERN RECOGNITION LAB
| Department of Electrical and Electronic Engineering
| Yonsei University 50 Yonsei-ro, Seodaemun-gu, Seoul 03722, Republic of Korea
| Email: paulyongju@yonsei.ac.kr
=====================================
'''

import cv2
import random
import numpy as np

def main():
        # 배경 이미지 사이즈 (세로, 가로)
    background_size = (256,256)

        # 원하는 사각형 사이즈 (세로, 가로)
    filter_size = (100,150)

        #channel 설정
    channel = 4

        # 메인 윈도우 생성
    main_window = make_rect(background_size)
    if channel == 4:
        b,g,r = cv2.split(main_window)
        alpha = np.ones(main_window.shape[:2], dtype=np.uint8) * 0
        main_window=cv2.merge((b,g,r,alpha))
    elif channel ==1:
        main_window = cv2.cvtColor(main_window,cv2.COLOR_BGR2GRAY)

        # 원하는 사각형 위치 세로, 가로 설정
    center_y = 50
    center_x = 50

        # 사각형 개수
    n = 5

        # 사각형 간격 조절
    interval = 5

    '''
    원하는 Color 사각형으로 하고 싶을 경우 (주석 해제하고 사용, 아래 Random Color은 주석처리)
    =================================================================
    '''
        # # 원하는 두가지 색 조절 (B, G, R, A) <= OpenCV라서 BGRA 순서로 해야합니다.
    # rect1 = make_rect(filter_size, (0, 0, 0,255))
    # rect2 = make_rect(filter_size, (75, 75, 75,255))
    #
        # # rect3 이런식으로 추가해도 됨 그러면 아래 배열에도 추가해줘야 한다.
    # rect = [rect1, rect2]   #사각형들 리스트화
    #
        # # n개의 사각형 배치
    # set_n_rect(main_window, rect, (center_y, center_x), n, interval, forward=True)

    '''
    랜덤한 Color 사각형으로 하고 싶을 경우 (주석 해제하고 사용, 위의 원하는 Color 주석처리)
    =================================================================
    '''
        # TODO: 테마 색 지정하기??


    c1 = random_color('yellow',threshold1=50, threshold2=70)
    c2 = random_color('black', threshold1=30,threshold2=70)
    c3 = random_color('red', threshold1=30, threshold2=70)
    ''' 
        # # 랜덤 두가지 색
            # Default = Normal, Else = black, red, blue, green, sky, navy, maroon, purple, yellow...
            # you can also ad your own code
        c1 = random_color('yellow',threshold1=50, threshold2=70)
            # 다른 사용법
            # alpha(투명도)
        c2 = random_color((255,255,255,255),threshold1=0,threshold2=0, threshold3=0) 각 threshold로 BGR variation 조절 alpha 조절 가능
        c2 = random_color((255,255,255),threshold1=0,threshold2=0, threshold3=0), 각 threshold로 BGR variation 조절 alpha 255 고정
        c2 = random_color((255,255),threshold1=0), black ~ white 조절, alpha 조절 가능
        c2 = random_color((255),threshold1=0), black ~ white 조절, alpha 255
    '''
    rect_r1 = make_rect(filter_size, c1)
    rect_r2 = make_rect(filter_size, c2)
    # rect_r3 = make_rect(filter_size, c3)

    rect_rand = [rect_r1, rect_r2]

        # if you want more colorful rect just add to below list
    # rect_rand = [rect_r1, rect_r2, rect_r3]

    set_n_rect(main_window, rect_rand, (center_y, center_x), n, interval, forward=True)
        # set_n_rect(src, rects, center, iter, interval, forward = True )
        # src - source that where you want to draw rectangles (numpy array ex) (512,512,4) or (512,512,3)
        # rects - list of rectangles
        # center - where you want to draw rectangles at (y,x) of src
        # iter - iteration of drawing rectangles
        # interval - x, y interval between rectangles
        # forward - True, False


    cv2.imwrite('test.png',main_window)
    cv2.imshow('window',main_window)
    cv2.waitKey(0)

def make_rect(size, color=(255,255,255,255)):
    width = size[0]
    height = size[1]
    if len(color)== 3:
        out = np.full((width,height,3),color,dtype=np.uint8)
    elif len(color)==1:
        out = np.full((width, height), color, dtype=np.uint8)
    elif len(color)== 4:
        out = np.full((width,height,4),color,dtype=np.uint8)
    return out

def set_rect(src,rect,points):
    src[points[0]:points[0]+rect.shape[0], points[1]:points[1]+rect.shape[1],:4] = rect

def set_n_rect(src, rects, center, iter, interval, forward = True ):
    if forward:
        for i in range(0, iter):
            set_rect(src, rects[i%len(rects)], (center[0] + i * interval, center[1] + i * interval))
    else:
        for i in range(0, iter):
            set_rect(src, rects[i%len(rects)], (center[0] + i * interval, center[1] - i * interval))

def random_color(templete = 'Normal', threshold1 = 75,threshold2 = 75, threshold3 = 75,channel = 4):
    if type(templete) == str:
        if templete =='Normal':
            color = (random.randint(0,255),random.randint(0,255), random.randint(0,255),255)
        elif templete == 'blue':
            color = (random.randint(255 - threshold1, 255), random.randint(0, threshold2), random.randint(0, threshold2),255)
        elif templete == 'sky':
            color = (random.randint(255 - threshold1, 255), random.randint(255 - threshold1, 255), random.randint(0, threshold2),255)
        elif templete == 'yellow':
            color = (random.randint(0, threshold2),random.randint(255 - threshold1, 255), random.randint(255 - threshold1, 255),255)
        elif templete == 'red':
            color = (random.randint(0, threshold2), random.randint(0, threshold2), random.randint(255 - threshold1, 255),255)
        elif templete == 'puple':
            color = (random.randint(255 - threshold1, 255), random.randint(0, threshold2), random.randint(255 - threshold1, 255),255)
        elif templete == 'navy':
            color = (random.randint(128 - threshold1, 128+threshold1), random.randint(0, threshold2), random.randint(0, threshold2),255)
        elif templete == 'maroon':
            color = (random.randint(0, threshold2), random.randint(0, threshold2),random.randint(128 - threshold1, 128+threshold1), 255)
        elif templete == 'green':
            color = (random.randint(0, threshold2), random.randint(255 - threshold1, 255), random.randint(0, threshold2), 255)
        elif templete == 'black':
            color = (random.randint(0, threshold2), random.randint(0, threshold2), random.randint(0, threshold2), 255)

    else:
        if len(templete)==4:
            color = (random.randint(templete[0] - threshold1, templete[0] + threshold1),
                     random.randint(templete[1] - threshold2, templete[1] + threshold2),
                     random.randint(templete[2] - threshold3, templete[2] + threshold3), templete[3])
        elif len(templete)==3:
            color = (random.randint(templete[0] - threshold1, templete[0] + threshold1),
                     random.randint(templete[1] - threshold2, templete[1] + threshold2),
                     random.randint(templete[2] - threshold3, templete[2] + threshold3), 255)
        elif len(templete)==2:
            color = (random.randint(templete[0] - threshold1, templete[0] + threshold1),
                     random.randint(templete[0] - threshold1, templete[0] + threshold1),
                     random.randint(templete[0] - threshold1, templete[0] + threshold1), templete[3])
        elif len(templete)==1:
            color = (random.randint(templete[0] - threshold1, templete[0] + threshold1),
                     random.randint(templete[0] - threshold1, templete[0] + threshold1),
                     random.randint(templete[0] - threshold1, templete[0] + threshold1), 255)
    if channel == 4:
        return color
    elif channel ==3:
        return color[:3]
    elif channel ==1:
        return color[0]

if __name__ == '__main__':
    main()
    # print(random_color())