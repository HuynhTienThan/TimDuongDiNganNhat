

from __future__ import print_function


def TaoMaTran():
    new = []
    new.append(0)
    new.append(1)
    new.append(1)
    new.append(1)
    new.append(0)
    new.append(0)
    new.append(0)
    MaTranKe.append(new)
    
    new = []
    new.append(1)
    new.append(0)
    new.append(0)
    new.append(0)
    new.append(0)
    new.append(0)
    new.append(0)
    MaTranKe.append(new)
    
    new = []
    new.append(1)
    new.append(0)
    new.append(0)
    new.append(0)
    new.append(1)
    new.append(1)
    new.append(0)
    MaTranKe.append(new)
    
    new = []
    new.append(1)
    new.append(0)
    new.append(0)
    new.append(0)
    new.append(0)
    new.append(0)
    new.append(1)
    MaTranKe.append(new)
    
    new = []
    new.append(0)
    new.append(0)
    new.append(1)
    new.append(0)
    new.append(0)
    new.append(0)
    new.append(0)
    MaTranKe.append(new)
    
    new = []
    new.append(0)
    new.append(0)
    new.append(1)
    new.append(0)
    new.append(0)
    new.append(0)
    new.append(0)
    MaTranKe.append(new)
    
    new = []
    new.append(0)
    new.append(0)
    new.append(0)
    new.append(1)
    new.append(0)
    new.append(0)
    new.append(0)
    MaTranKe.append(new)
def TaoDinh():
    for i in range(0,7):
        new=[]
        new.append(i)
        new.append(False)
        Dinh.append(new)
def LayDinhKe(vt):
    for i in range(0,7):
        if(MaTranKe[vt][i]==1 and Dinh[i][1]==False):
            TapDinhKe.append(i)
def BFS():
    Dinh[0][1]=True
    print(Dinh[0][0]+1)
    queue.append(Dinh[0][0])
    while(len(queue)!=0):
        DinhCanXet=queue.pop(0)
        LayDinhKe(DinhCanXet)
        while (len(TapDinhKe)!=0):
            DinhKe=TapDinhKe.pop(0)
            Dinh[DinhKe][1]=True
            print(DinhKe+1)
            queue.append(DinhKe)
    for i in range(0,7):
        Dinh[i][1]=False


queue = []
Dinh = []
MaTranKe = []
TapDinhKe = []
TaoMaTran()
TaoDinh()
print('Ma trận kề: ',MaTranKe)
print('các đỉnh',Dinh)
BFS()