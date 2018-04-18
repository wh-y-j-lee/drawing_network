# Made by YongJu Lee 18.04.09
# Version 2
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
    filter_size = (100,100)

        #channel 설정
    channel = 4

        # 메인 윈도우 생성
    dr_net = draw_net()
    main_window = dr_net.set_window(background_size)

    if channel == 4:
        b,g,r,a = cv2.split(main_window)
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
    # rect1 = dr_net.make_rect(filter_size, (0, 0, 0,255))
    # rect2 = dr_net.make_rect(filter_size, (75, 75, 75,255))
    #
        # # rect3 이런식으로 추가해도 됨 그러면 아래 배열에도 추가해줘야 한다.
    # rect = [rect1, rect2]   #사각형들 리스트화
    #
        # # n개의 사각형 배치
    # dr_net.set_n_rect(main_window, rect, (center_y, center_x), n, interval, forward=True)

    '''
    랜덤한 Color 사각형으로 하고 싶을 경우 (주석 해제하고 사용, 위의 원하는 Color 주석처리)
    =================================================================
    '''
        # TODO: 테마 색 지정하기??


    c1 = dr_net.random_color('yellow',threshold1=30, threshold2=70)
    c2 = dr_net.random_color('red', threshold1=30,threshold2=70)
    # c3 = dr_net.random_color('red', threshold1=30, threshold2=70)
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
    c1 = dr_net.random_color((255, 0,255,70), threshold1=0, threshold2=0, threshold3=0)
    c1 = dr_net.random_color((0, 0, 255, 70), threshold1=0, threshold2=0, threshold3=0)
    rect_r1 = dr_net.make_rect(filter_size, c1)
    rect_r2 = dr_net.make_rect(filter_size, c2)
    # rect_r3 = make_rect(filter_size, c3)

    rect_rand = [rect_r1, rect_r2]

        # if you want more colorful rect just add to below list
    # rect_rand = [rect_r1, rect_r2, rect_r3]

    dr_net.set_n_rect(main_window, rect_rand, (center_y, center_x), n, interval, forward=True)
        # dr_net.set_n_rect(src, rects, center, iter, interval, forward = True )
        # src - source that where you want to draw rectangles (numpy array ex) (512,512,4) or (512,512,3)
        # rects - list of rectangles
        # center - where you want to draw rectangles at (y,x) of src
        # iter - iteration of drawing rectangles
        # interval - x, y interval between rectangles
        # forward - True, False
    dr_net.set_3d_rect(main_window,(center_y,center_x),(100,50,100,45), 2 ,(75,75,75),1)

    cv2.imwrite('test.png',main_window)
    cv2.imshow('window',main_window)
    cv2.waitKey(0)
class draw_net():
    def set_window(self,background_size):
        main_window = self.make_rect(background_size)
        return main_window
    def make_rect(self,size, color=(255,255,255,255)):
        width = size[0]
        height = size[1]
        if len(color)== 3:
            out = np.full((width,height,3),color,dtype=np.uint8)
        elif len(color)==1:
            out = np.full((width, height), color, dtype=np.uint8)
        elif len(color)== 4:
            out = np.full((width,height,4),color,dtype=np.uint8)
        return out

    def set_rect(self,src,rect,points):
        src[points[0]:points[0]+rect.shape[0], points[1]:points[1]+rect.shape[1],:4] = rect

    def set_n_rect(self,src, rects, center, iter, interval, forward = True ):
        if forward:
            for i in range(0, iter):
                self.set_rect(src, rects[i%len(rects)], (center[0] + i * interval, center[1] + i * interval))
        else:
            for i in range(0, iter):
                self.set_rect(src, rects[i%len(rects)], (center[0] + i * interval, center[1] - i * interval))

    def random_color(self,templete = 'Normal', threshold1 = 75,threshold2 = 75, threshold3 = 75,channel = 4):
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
            elif templete == 'purple':
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
                         random.randint(templete[0] - threshold1, templete[0] + threshold1), templete[1])
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

    def set_3d_rect(self,src, center, size, interval, color=(255, 255, 255), direction=1):
        # size(width,height,length,angle)

        '''              '4  '5         '   '
                        '0  '1 '6      '   ''
                        '2  '3         '   '
        '''
        rect = self.make_rect(size[:2], color)
        width = size[0]
        height = size[1]
        length = size[2]
        if direction == 1:
            angle = size[3]
        elif direction == 2:
            angle = 180 - size[3]
        l_1 = int(length * np.cos(angle / 180 * np.pi))
        l_2 = int(length * np.sin(angle / 180 * np.pi))
        point_0 = center
        point_1 = (center[0] + size[1], center[1])
        point_2 = (center[0], center[1] + size[0])
        point_3 = (center[0] + size[1], center[1] + size[0])
        point_4 = (center[0] + l_1, center[1] - l_2)
        point_5 = (center[0] + l_1 + size[1], center[1] - l_2)
        if direction == 1:
            point_6 = (point_3[0] + l_1, point_3[1] - l_2)
        elif direction == 2:
            point_6 = (point_2[0] + l_1, point_2[1] - l_2)

        # TODO 1: 1st Rect (윗면)
        # if direction == 1:
        cv2.fillConvexPoly(src, np.array((point_0, point_1, point_5, point_4), dtype=int), color)
        # elif direction == 2:
        #     cv2.fillConvexPoly(src, np.array(((point_0[0]-interval,point_0[1]), (point_1[0]-interval,point_1[1]), point_5, point_4), dtype=int), color)
        # TODO 2: 2st Rect (정면)
        if direction == 1:
            self.set_rect(src, rect, (center[0] + interval, center[1] - interval))
        elif direction == 2:
            self.set_rect(src, rect, (center[0], center[1] + interval))
        # TODO 3: 3st Rect (옆면)
        if direction == 1:
            cv2.fillConvexPoly(src, np.array(
                ((point_1[0], point_1[1] + interval), point_3, point_6, (point_5[0], point_5[1] + interval)),
                dtype=int), color)
        elif direction == 2:
            cv2.fillConvexPoly(src, np.array(
                ((point_0[0], point_0[1] + interval), point_2, point_6, (point_4[0], point_4[1] + interval)),
                dtype=int), color)

if __name__ == '__main__':
    main()
    # print(random_color())