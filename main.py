
import math
import random
import pygame
import time
HangDoi = []
Dinh = []
MaTranKe = []
TapDinhKe = []
pos_yasuo=[]

pygame.init()
screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption('Tìm đường đi ngắn nhất')
clock=pygame.time.Clock()

WHITE=(255,255,255)
BLACK=(0,0,0)

yasuo=pygame.image.load('yasuo.png')
yasuo=pygame.transform.scale(yasuo,(50,50))
pos_yasuo_x=100
pos_yasuo_y=100
step=50

MuiTen=pygame.image.load('MuiTen.png')
MuiTen=pygame.transform.scale(MuiTen,(25,25))
pos_MuiTen_x=100
pos_MuiTen_y=100    

Bom=pygame.image.load('bom.png')
Bom=pygame.transform.scale(Bom,(50,50))
pos_Bom_1=[2000,2000]
pos_Bom_2=[2000,2000]
pos_Bom_3=[2000,2000]
pos_Bom_4=[2000,2000]
pos_Bom_5=[2000,2000]
pos_Bom_6=[2000,2000]
pos_Bom_7=[2000,2000]
pos_Bom_8=[2000,2000]
pos_Bom_9=[2000,2000]
pos_Bom_10=[2000,2000]
pos_Bom_11=[2000,2000]
pos_Bom_12=[2000,2000]
pos_Bom_13=[2000,2000]
pos_Bom_14=[2000,2000]

font=pygame.font.SysFont('sans',40)
text=font.render('Refresh', True, BLACK)


## Thuật toán tìm đường đi


def TaoMaTran():
    for i in range(0,112):
        new = []
        for j in range(0,112):
            new.append(0)
        MaTranKe.append(new)
    for i in range(1,13):
        MaTranKe[i][i+14]=1
        MaTranKe[i][i+1]=1
        MaTranKe[i][i-1]=1
    for i in range(99,111):
        MaTranKe[i][i-14]=1
        MaTranKe[i][i+1]=1
        MaTranKe[i][i-1]=1
    for i in range(14,98):
        if (i!=14 and i!=28 and i!=42 and i!=56 and i!=70 and i!=84 and i!=27 and i!=41 and i!=55 and i!=69 and i!=83 and i!=97):
            MaTranKe[i][i+1]=1
            MaTranKe[i][i-1]=1
            MaTranKe[i][i+14]=1
            MaTranKe[i][i-14]=1
    for i in range(14,85,14):
        MaTranKe[i][i+1]=1
        MaTranKe[i][i+14]=1
        MaTranKe[i][i-14]=1
    for i in range(27,98,14):
        MaTranKe[i][i-1]=1
        MaTranKe[i][i+14]=1
        MaTranKe[i][i-14]=1

    MaTranKe[0][1]=1
    MaTranKe[0][14]=1

    MaTranKe[13][12]=1
    MaTranKe[13][27]=1

    MaTranKe[98][84]=1
    MaTranKe[98][99]=1

    MaTranKe[111][97]=1
    MaTranKe[111][110]=1


    
def TaoDinh():
    for i in range(0,112):
        new=[]
        new.append(i)
        new.append(False)
        Dinh.append(new)
def LayDinhKe(vt):
    for i in range(0,112):
        if(MaTranKe[vt][i]==1 and Dinh[i][1]==False):
            TapDinhKe.append(i)
def LayToaDo(SoDinh):
    new=[]
    dem=0
    step_Y=0
    
    for i in range(0,112):
        
        if dem==14:
            dem=0
            step_Y=step_Y+50
        if i==SoDinh:
            new.append(100 + dem*50)
            new.append(100 + step_Y)
            pos_yasuo.append(new)
            return
        dem=dem+1
def LayToaDoReturn(SoDinh):
    dem=0
    step_Y=0
    ToaDoLocal=[]
    for i in range(0,112):
        
        if dem==14:
            dem=0
            step_Y=step_Y+50
        if i==SoDinh:
            ToaDoLocal.append(100 + dem*50)
            ToaDoLocal.append(100 + step_Y)
            return ToaDoLocal
        dem=dem+1
def LayDinh(ToaDoDinh_x,ToaDoDinh_y):
    for i in range(0,112):
        if LayToaDoReturn(i)==[ToaDoDinh_x,ToaDoDinh_y]:
            return i
Goal=111
Start=2
ViTriHienTai_x=100
ViTriHienTai_y=100
def BFS():
    global Goal,Start
    KhoangCach=[]
    ToaDo=[]
    def KhoangCachNganNhat():
        min=KhoangCach[0]
        for i in range(0,len(KhoangCach)):
            if KhoangCach[i]<min:
                min=KhoangCach[i]
        for i in range(0,len(KhoangCach)):
            if KhoangCach[i]==min:
                KhoangCach.clear()
                return i
    Dinh[Start][1]=True
    # print(Dinh[0][0])
    HangDoi.append(Dinh[Start][0])
    while(len(HangDoi)!=0):
        DinhCanXet=HangDoi.pop(0)
        LayDinhKe(DinhCanXet)
        while(len(TapDinhKe)!=0):
            # print("Tập đỉnh kề: ",TapDinhKe)
            for i in range(0,len(TapDinhKe)):
                Dinh[TapDinhKe[i]][1]=True
            for i in range(0,len(TapDinhKe)):
                ToaDo=LayToaDoReturn(TapDinhKe[i])
                ToaDoDich=LayToaDoReturn(Goal)
                # print("Tọa độ: ",ToaDo[0],"  ",ToaDo[1])
                KhoangCach.append(math.sqrt((ToaDo[0]-ToaDoDich[0])**2+(ToaDo[1]-ToaDoDich[1])**2))
                # print("Khoảng Cách",KhoangCach)
            KCachNganNhat=KhoangCachNganNhat()
            # print(KCachNganNhat)
            for i in range(0,len(TapDinhKe)):
                if i==KCachNganNhat:
                    DinhKe=TapDinhKe[i]
                    TapDinhKe.clear()
                    break
            # print(DinhKe)
            # DinhKe=TapDinhKe.pop(0)
            LayToaDo(DinhKe)
            if DinhKe==Goal:
                break
            # print("Đỉnh kề: ",DinhKe)
            # print("Tập tọa đô đường đi: ",pos_yasuo)
            # print("Vị Trí yasuo: ",pos_yasuo_x,"  ",pos_yasuo_y)
            # print("Hảng đợi: ",HangDoi)
            HangDoi.append(DinhKe)
    for i in range(0,112):
        Dinh[i][1]=False



TaoMaTran()
TaoDinh()
# BFS
running=True
while running:
    clock.tick(600)
    screen.fill((0,204,136))

    mouse_x, mouse_y=pygame.mouse.get_pos()
    # print(mouse_pos)
    #Ve Duong line
    pygame.draw.rect(screen, WHITE, (100,100,700,400))
    for i in range(100,501,50):
        pygame.draw.line(screen, BLACK, (100,i),(800,i),width=5)    
    for i in range(100,801,50):
        pygame.draw.line(screen, BLACK, (i,100),(i,500),width=5)   

    #Chuong ngai vat
    screen.blit(Bom,(pos_Bom_1[0],pos_Bom_1[1]))
    screen.blit(Bom,(pos_Bom_2[0],pos_Bom_2[1]))
    screen.blit(Bom,(pos_Bom_3[0],pos_Bom_3[1]))
    screen.blit(Bom,(pos_Bom_4[0],pos_Bom_4[1]))
    screen.blit(Bom,(pos_Bom_5[0],pos_Bom_5[1]))
    screen.blit(Bom,(pos_Bom_6[0],pos_Bom_6[1]))
    screen.blit(Bom,(pos_Bom_7[0],pos_Bom_7[1]))
    screen.blit(Bom,(pos_Bom_8[0],pos_Bom_8[1]))
    screen.blit(Bom,(pos_Bom_9[0],pos_Bom_9[1]))
    screen.blit(Bom,(pos_Bom_10[0],pos_Bom_10[1]))
    screen.blit(Bom,(pos_Bom_11[0],pos_Bom_11[1]))
    screen.blit(Bom,(pos_Bom_12[0],pos_Bom_12[1]))
    screen.blit(Bom,(pos_Bom_13[0],pos_Bom_13[1]))
    screen.blit(Bom,(pos_Bom_14[0],pos_Bom_14[1]))

    #Ve yasuo
    screen.blit(yasuo,(pos_yasuo_x,pos_yasuo_y))
    #Ve Mui Ten
    screen.blit(MuiTen,(pos_MuiTen_x+12.5,pos_MuiTen_y+12.5))
    if (pos_MuiTen_x==pos_yasuo_x and pos_MuiTen_y==pos_yasuo_y):
        pos_MuiTen_x=2000
        pos_MuiTen_y=2000

    pygame.draw.rect(screen, 'gray', (850,125,125,50))
    screen.blit(text,(855,125))
    


    # DiChuyen()
    if (pos_yasuo_x==ViTriHienTai_x and pos_yasuo_y==ViTriHienTai_y):
        vt=0
    if(vt < len(pos_yasuo)):
        if (pos_yasuo_x < pos_yasuo[vt][0]):
            pos_yasuo_x = pos_yasuo_x + 1
        if (pos_yasuo_x > pos_yasuo[vt][0]):
            pos_yasuo_x = pos_yasuo_x - 1
        if(pos_yasuo_y < pos_yasuo[vt][1]):
            pos_yasuo_y = pos_yasuo_y + 1
        if(pos_yasuo_y > pos_yasuo[vt][1]):
            pos_yasuo_y = pos_yasuo_y - 1
        if(pos_yasuo_x==pos_yasuo[vt][0] and pos_yasuo_y==pos_yasuo[vt][1]):
            # pygame.draw.rect(screen, 'red', (pos_yasuo[vt][0],pos_yasuo[vt][1],50,50))
            vt=vt+1
        if(vt==len(pos_yasuo)):
            pos_yasuo.clear()



    # key_input = pygame.key.get_pressed()   nhấn giữ
    # if key_input[pygame.K_LEFT]:
    #     pos_yasuo_x -= step
    # if key_input[pygame.K_UP]:
    #     pos_yasuo_y -= step
    # if key_input[pygame.K_RIGHT]:
    #     pos_yasuo_x += step
    # if key_input[pygame.K_DOWN]:
    #     pos_yasuo_y += step
    



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN: # nhấn 1 lần
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if(pos_yasuo_x==100):
                    break
                else:
                    pos_yasuo_x -= step
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if(pos_yasuo_x==750):
                    break
                else:
                    pos_yasuo_x += step
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if(pos_yasuo_y==100):
                    break
                else:
                    pos_yasuo_y -= step
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if(pos_yasuo_y==450):
                    break
                else:
                    pos_yasuo_y += step
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if((mouse_x >= 850 and mouse_x <= 975) and (mouse_y >= 125 and mouse_y <=175)):
                if mouse_presses[0]:
                    Diem_xuat_phat_ngau_nhien=random.randint(0,111)
                    Toa_do_Diem_xuat_phat_ngau_nhien=LayToaDoReturn(Diem_xuat_phat_ngau_nhien)
                    pos_yasuo_x,pos_yasuo_y=Toa_do_Diem_xuat_phat_ngau_nhien
                    
                    TaoMaTran()
                    DinhBom1=random.randint(0,111)
                    DinhBom2=random.randint(0,111)
                    DinhBom3=random.randint(0,111)
                    DinhBom4=random.randint(0,111)
                    DinhBom5=random.randint(0,111)
                    DinhBom6=random.randint(0,111)
                    DinhBom7=random.randint(0,111)
                    DinhBom8=random.randint(0,111)
                    DinhBom9=random.randint(0,111)
                    DinhBom10=random.randint(0,111)
                    DinhBom11=random.randint(0,111)
                    DinhBom12=random.randint(0,111)
                    DinhBom13=random.randint(0,111)
                    DinhBom14=random.randint(0,111)

                    pos_Bom_1=LayToaDoReturn(DinhBom1)
                    pos_Bom_2=LayToaDoReturn(DinhBom2)
                    pos_Bom_3=LayToaDoReturn(DinhBom3)
                    pos_Bom_4=LayToaDoReturn(DinhBom4)
                    pos_Bom_5=LayToaDoReturn(DinhBom5)
                    pos_Bom_6=LayToaDoReturn(DinhBom6)
                    pos_Bom_7=LayToaDoReturn(DinhBom7)
                    pos_Bom_8=LayToaDoReturn(DinhBom8)
                    pos_Bom_9=LayToaDoReturn(DinhBom9)
                    pos_Bom_10=LayToaDoReturn(DinhBom10)
                    pos_Bom_11=LayToaDoReturn(DinhBom11)
                    pos_Bom_12=LayToaDoReturn(DinhBom12)
                    pos_Bom_13=LayToaDoReturn(DinhBom13)
                    pos_Bom_14=LayToaDoReturn(DinhBom14)

                    for i in range(0,112):
                        MaTranKe[DinhBom1][i]=0
                        MaTranKe[DinhBom2][i]=0
                        MaTranKe[DinhBom3][i]=0
                        MaTranKe[DinhBom4][i]=0
                        MaTranKe[DinhBom5][i]=0
                        MaTranKe[DinhBom6][i]=0
                        MaTranKe[DinhBom7][i]=0
                        MaTranKe[DinhBom8][i]=0
                        MaTranKe[DinhBom9][i]=0
                        MaTranKe[DinhBom10][i]=0
                        MaTranKe[DinhBom11][i]=0
                        MaTranKe[DinhBom12][i]=0
                        MaTranKe[DinhBom13][i]=0
                        MaTranKe[DinhBom14][i]=0
                    
                        MaTranKe[i][DinhBom1]=0
                        MaTranKe[i][DinhBom2]=0
                        MaTranKe[i][DinhBom3]=0
                        MaTranKe[i][DinhBom4]=0
                        MaTranKe[i][DinhBom5]=0
                        MaTranKe[i][DinhBom6]=0
                        MaTranKe[i][DinhBom7]=0
                        MaTranKe[i][DinhBom8]=0
                        MaTranKe[i][DinhBom9]=0
                        MaTranKe[i][DinhBom10]=0
                        MaTranKe[i][DinhBom11]=0
                        MaTranKe[i][DinhBom12]=0
                        MaTranKe[i][DinhBom13]=0
                        MaTranKe[i][DinhBom14]=0
            for i in range(0,112):
                x,y=LayToaDoReturn(i)
                if((mouse_x>x and mouse_x<x+50) and (mouse_y > y and mouse_y < y+50)):
                    if mouse_presses[0]:
                        pos_MuiTen_x=x
                        pos_MuiTen_y=y
                        ViTriHienTai_x=pos_yasuo_x
                        ViTriHienTai_y=pos_yasuo_y
                        Goal=LayDinh(x,y)
                        Start=LayDinh(pos_yasuo_x,pos_yasuo_y)
                        BFS()
                        break
    pygame.display.flip()
pygame.quit()