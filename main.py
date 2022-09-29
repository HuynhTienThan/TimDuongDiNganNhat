import math
import random
import pygame
import time

LuaChon="BatDau"

HangDoi = []
Dinh = []
MaTranKe = []
TapDinhKe = []
pos_yasuo=[]
vt=0

HangDoiMeCung = []
DinhMeCung = []
MaTranKeMeCung = []
TapDinhKeMeCung = []
pos_irelia_MeCung=[]
vtMeCung=0


pygame.init()
screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption('Tìm đường đi ngắn nhất')
clock=pygame.time.Clock()

WHITE=(255,255,255)
BLACK=(0,0,0)
MAUDUONGLINE=(16,54,103)
WidtLine=4

AnhNen=pygame.image.load('BackgroundSelection.PNG')
AnhNen=pygame.transform.scale(AnhNen,(1000,600))

BackgroundYS=pygame.image.load('backgroundYS.jpg')
BackgroundYS=pygame.transform.scale(BackgroundYS,(700,400))

Back=pygame.image.load('back.png')
Back=pygame.transform.scale(Back,(30,30))

yasuo=pygame.image.load('yasuo.png')
yasuo=pygame.transform.scale(yasuo,(50,50))
pos_yasuo_x=100
pos_yasuo_y=100
yone=pygame.image.load('yone.png')
yone=pygame.transform.scale(yone,(20,20))
pos_yone_x=100
pos_yone_y=50
step=50
step_yone=20

pos_tick_x=10000
pos_tick_y=10000
ListTick=[]

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
def BFSThongMinh():
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
        while len(TapDinhKe)==0:
            a=pos_yasuo.pop()
            LayDinhKe(LayDinh(a[0],a[1]))
        while(len(TapDinhKe)!=0):
            # print("Tập đỉnh kề: ",TapDinhKe)
            # for i in range(0,len(TapDinhKe)):
            #     Dinh[TapDinhKe[i]][1]=True
            for i in range(0,len(TapDinhKe)):
                ToaDo=LayToaDoReturn(TapDinhKe[i])
                ToaDoDich=LayToaDoReturn(Goal)
                # print("Tọa độ: ",ToaDo[0],"  ",ToaDo[1])
                KhoangCach.append(math.sqrt((ToaDo[0]-ToaDoDich[0])**2+(ToaDo[1]-ToaDoDich[1])**2))
                # print("Khoảng Cách",KhoangCach)
            KCachNganNhat=KhoangCachNganNhat()
            # print(KCachNganNhat)
            Dinh[TapDinhKe[KCachNganNhat]][1]=True
            DinhKe=TapDinhKe[KCachNganNhat]
            TapDinhKe.clear()
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
def BFS():
    global Goal,Start
    print("Start = ",Start,"Goal = ",Goal)
    Dinh[Start][1]=True
    # print(Dinh[0][0])
    HangDoi.append(Dinh[Start][0])
    print(Dinh[Start][0])
    print(HangDoi)
    while(len(HangDoi)!=0):
        DinhCanXet=HangDoi.pop(0)
        LayDinhKe(DinhCanXet)
        print(TapDinhKe,"Dinh can xet: ",DinhCanXet)
        while(len(TapDinhKe)!=0):
            # print("Tập đỉnh kề: ",TapDinhKe)
            DinhKe=TapDinhKe.pop(0)
            Dinh[DinhKe][1]=True
            LayToaDo(DinhKe)
            if(DinhKe==Goal):
                TapDinhKe.clear()
                for i in range (0,len(pos_yasuo)):
                    print(LayDinh(pos_yasuo[i][0],pos_yasuo[i][1]))
                print(pos_yasuo)
                for i in range(0,112):
                    Dinh[i][1]=False
                HangDoi.clear()
                return
            HangDoi.append(DinhKe)
                # print("Tọa độ: ",ToaDo[0],"  ",ToaDo[1])
            # print(DinhKe)
            # DinhKe=TapDinhKe.pop(0)
            # print("Đỉnh kề: ",DinhKe)
            # print("Tập tọa đô đường đi: ",pos_yasuo)
            # print("Vị Trí yasuo: ",pos_yasuo_x,"  ",pos_yasuo_y)
            # print("Hảng đợi: ",HangDoi)




TaoMaTran()
TaoDinh()
# BFSThongMinh
running=True
while running:
    clock.tick(300)
    # screen.fill('white')
    

    mouse_x, mouse_y=pygame.mouse.get_pos()
    if(LuaChon=="NganNhat"):
        #Ve Duong line
        # screen.blit(BackgroundYS,(100,100))
        pygame.draw.rect(screen, (148,170,214), (100,100,700,400))
        for i in range(100,501,50):
            if(i==100 or i==500):
                pygame.draw.line(screen, (16,54,103), (100,i),(800,i),width=5) 
            pygame.draw.line(screen, (16,54,103), (100,i),(800,i),width=2)    
        for i in range(100,801,50):
            if(i==100 or i==800):
                pygame.draw.line(screen, (16,54,103), (i,100),(i,500),width=5) 
            pygame.draw.line(screen, (16,54,103), (i,100),(i,500),width=1)   

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

        screen.blit(Back,(10,10))


        pygame.draw.rect(screen, 'gray', (850,125,125,50))
        screen.blit(text,(855,125))
        

        if(ListTick!=0):
            # for i in range(len(ListTick)-1):

            for i in range(len(ListTick)-1):
                pygame.draw.circle(screen, 'green', [ListTick[i][0]+25,ListTick[i][1]+25],10)
                pygame.draw.line(screen, 'white', (ListTick[i][0]+25,ListTick[i][1]+25),(ListTick[i+1][0]+25,ListTick[i+1][1]+25),width=2)   


        # DiChuyen()
        # if (pos_yasuo_x==ViTriHienTai_x and pos_yasuo_y==ViTriHienTai_y):
        #     vt=0
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
                new=[]
                new.append(pos_yasuo_x)
                new.append(pos_yasuo_y)
                ListTick.append(new)
                vt=vt+1
            if(vt==len(pos_yasuo)):
                pos_yasuo.clear()
    elif LuaChon=="MeCung":
        screen.fill('white')
        pygame.draw.rect(screen, (148,170,214), (100,50,600,440))

        screen.blit(yone,(pos_yone_x,pos_yone_y))


        for i in range(50,491,20):
            if(i==50 or i==490):
                pygame.draw.line(screen, MAUDUONGLINE, (100,i),(700,i),width=5) 
            if(i==70):
                pygame.draw.line(screen, MAUDUONGLINE, (140,i),(220,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (280,i),(300,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (320,i),(380,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (400,i),(440,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (460,i),(500,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (520,i),(540,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (560,i),(620,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (640,i),(680,i),width=WidtLine)  
            if(i==90):
                pygame.draw.line(screen, MAUDUONGLINE, (200,i),(220,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (260,i),(280,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (300,i),(320,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (380,i),(420,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (440,i),(480,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (500,i),(560,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (580,i),(680,i),width=WidtLine)    
            if(i==110):
                pygame.draw.line(screen, MAUDUONGLINE, (160,i),(220,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (240,i),(260,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (280,i),(300,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (320,i),(360,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (420,i),(440,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (480,i),(500,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (540,i),(580,i),width=WidtLine)    
                pygame.draw.line(screen, MAUDUONGLINE, (600,i),(620,i),width=WidtLine)  
            if i==130:
                pygame.draw.line(screen, MAUDUONGLINE, (100,i),(120,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (180,i),(200,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (260,i),(280,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (320,i),(340,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (360,i),(400,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (460,i),(520,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (560,i),(600,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (620,i),(700,i),width=WidtLine)  
            if i==150:
                pygame.draw.line(screen, MAUDUONGLINE, (120,i),(160,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (180,i),(200,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (240,i),(260,i),width=WidtLine) 
                pygame.draw.line(screen, MAUDUONGLINE, (340,i),(360,i),width=WidtLine) 
                pygame.draw.line(screen, MAUDUONGLINE, (400,i),(420,i),width=WidtLine) 
                pygame.draw.line(screen, MAUDUONGLINE, (500,i),(540,i),width=WidtLine) 
                pygame.draw.line(screen, MAUDUONGLINE, (580,i),(600,i),width=WidtLine) 
                pygame.draw.line(screen, MAUDUONGLINE, (620,i),(660,i),width=WidtLine) 
            if i==170:
                pygame.draw.line(screen, MAUDUONGLINE, (100,i),(180,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (200,i),(240,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (300,i),(320,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (340,i),(400,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (420,i),(440,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (480,i),(520,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (560,i),(580,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (600,i),(620,i),width=WidtLine)  
            if i==190:
                pygame.draw.line(screen, MAUDUONGLINE, (120,i),(140,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (180,i),(200,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (300,i),(320,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (360,i),(380,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (520,i),(600,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (640,i),(680,i),width=WidtLine)  
            if i==210:
                pygame.draw.line(screen, MAUDUONGLINE, (160,i),(180,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (200,i),(220,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (240,i),(300,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (340,i),(360,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (380,i),(420,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (460,i),(480,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (520,i),(580,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (640,i),(680,i),width=WidtLine)  
            if i==230:
                pygame.draw.line(screen, MAUDUONGLINE, (120,i),(160,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (220,i),(280,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (340,i),(380,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (400,i),(420,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (460,i),(480,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (540,i),(560,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (620,i),(660,i),width=WidtLine)  
            if i==250:
                pygame.draw.line(screen, MAUDUONGLINE, (100,i),(140,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (160,i),(200,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (240,i),(300,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (320,i),(400,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (420,i),(560,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (600,i),(620,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (660,i),(680,i),width=WidtLine)  
            if i==270:
                pygame.draw.line(screen, MAUDUONGLINE, (120,i),(140,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (180,i),(260,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (300,i),(320,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (340,i),(360,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (400,i),(420,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (440,i),(460,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (480,i),(500,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (540,i),(580,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (600,i),(640,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (680,i),(700,i),width=WidtLine)  
            if i==290:
                pygame.draw.line(screen, MAUDUONGLINE, (100,i),(120,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (160,i),(180,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (220,i),(260,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (300,i),(320,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (360,i),(380,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (400,i),(460,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (520,i),(560,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (580,i),(600,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (620,i),(660,i),width=WidtLine)  
            if i==310:
                pygame.draw.line(screen, MAUDUONGLINE, (120,i),(140,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (180,i),(200,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (220,i),(240,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (280,i),(300,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (340,i),(360,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (340,i),(360,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (380,i),(440,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (560,i),(580,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (620,i),(680,i),width=WidtLine) 
            if i==330:
                pygame.draw.line(screen, MAUDUONGLINE, (120,i),(160,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (180,i),(240,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (260,i),(320,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (360,i),(380,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (440,i),(460,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (480,i),(520,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (540,i),(660,i),width=WidtLine)  
            if i==350:
                pygame.draw.line(screen, MAUDUONGLINE, (120,i),(140,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (160,i),(200,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (240,i),(280,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (300,i),(320,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (380,i),(420,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (440,i),(480,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (500,i),(620,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (640,i),(680,i),width=WidtLine)  
            if i==370:
                pygame.draw.line(screen, MAUDUONGLINE, (120,i),(140,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (200,i),(240,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (320,i),(340,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (360,i),(380,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (420,i),(440,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (560,i),(600,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (640,i),(660,i),width=WidtLine)  
            if i==390:
                pygame.draw.line(screen, MAUDUONGLINE, (100,i),(120,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (140,i),(160,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (180,i),(240,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (340,i),(500,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (520,i),(580,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (620,i),(660,i),width=WidtLine)  
            if i==410:
                pygame.draw.line(screen, MAUDUONGLINE, (160,i),(180,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (220,i),(260,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (360,i),(400,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (460,i),(500,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (560,i),(600,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (660,i),(680,i),width=WidtLine)  
            if i==430:
                pygame.draw.line(screen, MAUDUONGLINE, (120,i),(140,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (200,i),(240,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (320,i),(360,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (380,i),(420,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (440,i),(460,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (480,i),(520,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (680,i),(700,i),width=WidtLine)  
            if i==450:
                pygame.draw.line(screen, MAUDUONGLINE, (140,i),(180,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (240,i),(320,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (340,i),(380,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (420,i),(440,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (460,i),(480,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (500,i),(560,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (580,i),(640,i),width=WidtLine)  
            if i==470:
                pygame.draw.line(screen, MAUDUONGLINE, (120,i),(160,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (300,i),(340,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (360,i),(420,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (480,i),(540,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (560,i),(580,i),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (620,i),(680,i),width=WidtLine)  
                
            pygame.draw.line(screen, (16,54,103), (100,i),(700,i),width=1)  

                

              
  
        for i in range(100,701,20):
            if(i==100 or i==700):
                pygame.draw.line(screen, MAUDUONGLINE, (i,50),(i,490),width=5) 
            if i==120:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,130),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,190),(i,230),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,310),(i,330),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,370),(i,390),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,410),(i,430),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,450),(i,470),width=WidtLine)  
            if i==140:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,150),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,190),(i,210),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,270),(i,310),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,350),(i,370),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,390),(i,450),width=WidtLine) 
            if i==160:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,90),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,110),(i,150),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,170),(i,210),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,230),(i,390),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,410),(i,430),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,470),(i,490),width=WidtLine)  
            if i==180:
                pygame.draw.line(screen, MAUDUONGLINE, (i,90),(i,110),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,150),(i,190),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,210),(i,230),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,310),(i,330),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,370),(i,410),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,430),(i,470),width=WidtLine)  
            if i==200:
                pygame.draw.line(screen, MAUDUONGLINE, (i,130),(i,150),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,190),(i,250),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,270),(i,310),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,350),(i,370),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,390),(i,470),width=WidtLine)  
            if i==220:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,90),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,110),(i,210),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,230),(i,270),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,330),(i,350),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,450),(i,490),width=WidtLine)  
            if i==240:
                pygame.draw.line(screen, MAUDUONGLINE, (i,50),(i,150),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,170),(i,210),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,310),(i,330),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,350),(i,370),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,430),(i,470),width=WidtLine)  
            if i==260:
                pygame.draw.line(screen, MAUDUONGLINE, (i,50),(i,70),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,90),(i,110),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,150),(i,190),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,270),(i,330),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,370),(i,430),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,470),(i,490),width=WidtLine)  
            if i==280:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,90),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,110),(i,210),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,250),(i,310),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,350),(i,430),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,470),(i,490),width=WidtLine)  
            if i==300:
                pygame.draw.line(screen, MAUDUONGLINE, (i,90),(i,150),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,170),(i,190),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,210),(i,250),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,270),(i,290),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,330),(i,450),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,470),(i,490),width=WidtLine)  
            if i==320:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,90),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,130),(i,170),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,190),(i,270),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,290),(i,330),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,370),(i,410),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,430),(i,450),width=WidtLine)  
            if i==340:
                pygame.draw.line(screen, MAUDUONGLINE, (i,90),(i,110),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,130),(i,150),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,170),(i,210),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,270),(i,370),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,390),(i,410),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,450),(i,470),width=WidtLine)  
            if i==360:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,90),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,110),(i,130),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,150),(i,170),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,310),(i,350),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,410),(i,430),width=WidtLine)  
            if i==380:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,110),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,130),(i,150),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,190),(i,230),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,250),(i,310),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,350),(i,370),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,430),(i,450),width=WidtLine)  
            if i==400:
                pygame.draw.line(screen, MAUDUONGLINE, (i,50),(i,70),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,90),(i,130),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,150),(i,190),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,230),(i,250),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,270),(i,290),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,310),(i,350),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,370),(i,390),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,430),(i,470),width=WidtLine)  
            if i==420:
                pygame.draw.line(screen, MAUDUONGLINE, (i,110),(i,150),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,170),(i,210),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,250),(i,270),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,310),(i,330),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,350),(i,370),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,390),(i,430),width=WidtLine)  
            if i==440:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,110),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,130),(i,250),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,350),(i,370),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,390),(i,410),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,430),(i,470),width=WidtLine)  
            if i==460:
                pygame.draw.line(screen, MAUDUONGLINE, (i,110),(i,210),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,270),(i,330),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,370),(i,390),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,410),(i,450),width=WidtLine)  
            if i==480:
                pygame.draw.line(screen, MAUDUONGLINE, (i,90),(i,110),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,150),(i,190),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,210),(i,230),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,270),(i,370),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,450),(i,470),width=WidtLine)  
            if i==500:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,90),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,130),(i,150),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,170),(i,250),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,270),(i,310),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,350),(i,390),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,430),(i,450),width=WidtLine)  
            if i==520:
                pygame.draw.line(screen, MAUDUONGLINE, (i,50),(i,70),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,90),(i,130),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,190),(i,230),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,250),(i,330),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,370),(i,430),width=WidtLine)  
            if i==540:
                pygame.draw.line(screen, MAUDUONGLINE, (i,110),(i,130),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,150),(i,190),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,310),(i,370),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,410),(i,450),width=WidtLine)  
            if i==560:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,90),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,130),(i,170),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,230),(i,250),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,290),(i,310),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,370),(i,390),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,410),(i,430),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,450),(i,470),width=WidtLine)  
            if i==580:
                pygame.draw.line(screen, MAUDUONGLINE, (i,90),(i,110),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,150),(i,170),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,210),(i,290),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,430),(i,470),width=WidtLine)  
            if i==600:
                pygame.draw.line(screen, MAUDUONGLINE, (i,110),(i,130),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,170),(i,190),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,210),(i,270),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,290),(i,330),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,370),(i,430),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,470),(i,490),width=WidtLine)  
            if i==620:
                pygame.draw.line(screen, MAUDUONGLINE, (i,70),(i,90),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,110),(i,130),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,150),(i,230),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,270),(i,290),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,350),(i,430),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,450),(i,470),width=WidtLine)  
            if i==640:
                pygame.draw.line(screen, MAUDUONGLINE, (i,50),(i,70),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,90),(i,110),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,170),(i,210),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,230),(i,250),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,410),(i,450),width=WidtLine)  
            if i==660:
                pygame.draw.line(screen, MAUDUONGLINE, (i,110),(i,130),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,150),(i,170),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,230),(i,290),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,330),(i,350),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,370),(i,390),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,410),(i,470),width=WidtLine)  
            if i==680:
                pygame.draw.line(screen, MAUDUONGLINE, (i,90),(i,110),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,130),(i,190),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,210),(i,230),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,270),(i,330),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,350),(i,410),width=WidtLine)  
                pygame.draw.line(screen, MAUDUONGLINE, (i,430),(i,450),width=WidtLine)  

            pygame.draw.line(screen, MAUDUONGLINE, (i,50),(i,490),width=1)   


                


    else:
        screen.blit(AnhNen,(0,0))


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
        if(LuaChon=="NganNhat"):
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
                if((mouse_x >= 10 and mouse_x <= 30) and (mouse_y >= 10 and mouse_y <=30)):
                    if mouse_presses[0]:
                        LuaChon="BatDau"
                if((mouse_x >= 850 and mouse_x <= 975) and (mouse_y >= 125 and mouse_y <=175)):
                    if mouse_presses[0]:
                        Diem_xuat_phat_ngau_nhien=random.randint(0,111)
                        Toa_do_Diem_xuat_phat_ngau_nhien=LayToaDoReturn(Diem_xuat_phat_ngau_nhien)
                        pos_yasuo_x,pos_yasuo_y=Toa_do_Diem_xuat_phat_ngau_nhien
                        
                        TaoMaTran()
                        DinhBom1=33
                        DinhBom2=48
                        DinhBom3=61
                        DinhBom4=32
                        DinhBom5=60
                        # DinhBom4=random.randint(0,111)
                        # DinhBom5=random.randint(0,111)
                        DinhBom6=4
                        DinhBom7=17
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
                            vt=0
                            ListTick.clear()
                            pos_MuiTen_x=x
                            pos_MuiTen_y=y
                            ViTriHienTai_x=pos_yasuo_x
                            ViTriHienTai_y=pos_yasuo_y
                            Goal=LayDinh(x,y)
                            Start=LayDinh(ViTriHienTai_x,ViTriHienTai_y)
                            starTime=time.time()
                            # BFS() 
                            BFSThongMinh()
                            endTime=time.time()
                            print(pos_yasuo)
                            HangDoi.clear()
                            TapDinhKe.clear()
                            # print("endTime = ",endTime,"starTime = ",starTime)
                            # print("endTime-starTime = ",endTime-starTime)
                            break
        elif LuaChon=="MeCung":
                if event.type == pygame.KEYDOWN: # nhấn 1 lần
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if(pos_yone_x==100):
                            break
                        else:
                            pos_yone_x -= step_yone
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if(pos_yone_x==680):
                            break
                        else:
                            pos_yone_x += step_yone
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if(pos_yone_y==50):
                            break
                        else:
                            pos_yone_y -= step_yone
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if(pos_yone_y==470):
                            break
                        else:
                            pos_yone_y += step_yone
        elif LuaChon=="BatDau":
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if((mouse_x >= 288 and mouse_x <= 713) and (mouse_y >= 169 and mouse_y <=244)):
                    if mouse_presses[0]:
                        LuaChon="NganNhat"
                if((mouse_x >= 288 and mouse_x <= 713) and (mouse_y >= 316 and mouse_y <=387)):
                    if mouse_presses[0]:
                        LuaChon="MeCung"
            
    pygame.display.flip()
pygame.quit()
