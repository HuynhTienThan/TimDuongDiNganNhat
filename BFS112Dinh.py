


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
def BFS():
    Dinh[0][1]=True
    print(Dinh[0][0])
    queue.append(Dinh[0][0])
    while(len(queue)!=0):
        DinhCanXet=queue.pop(0)
        LayDinhKe(DinhCanXet)
        while (len(TapDinhKe)!=0):
            DinhKe=TapDinhKe.pop(0)
            Dinh[DinhKe][1]=True
            print(DinhKe)
            # if(DinhKe==17):
            #     return
            queue.append(DinhKe)
    for i in range(0,112):
        Dinh[i][1]=False


queue = []
Dinh = []
MaTranKe = []
TapDinhKe = []
TaoMaTran()
TaoDinh()
BFS()