
# coding: utf-8

# In[68]:



def splitT(s):
    # split time:
    # format T:[h,m,s,ms]
    T = s.split(',')[0].split(":")
    T.append(s.split(',')[1])
    
    # transform to ms, then subtract time
    TotalT = int(T[0])*60*60*1000 + int(T[1])*60*1000 + int(T[2])*1000 +int(T[3])
    TotalT -= subTime
    
    # reder back to H:M:S,MS:
    ms = TotalT%1000
    TotalT /= 1000;
    H = int(TotalT/(60*60))
    TotalT -= 60*60*H
    M = int(TotalT/60)
    TotalT -= 60 * M
    S = int(TotalT)
    Tstr= "{:0>2}:{:0>2}:{:0>2},{:0>3}".format(H, M, S, ms)
    return Tstr
        



f = open("GIS.srt",encoding = "latin-1")
fnew = open("GISNew.srt",'w', encoding = "latin-1")
subTime = 11270
Num = 2
for line in f:
    if line=="1\n":
        print("here")
        line = next(f)
        line = next(f)
        line = next(f)
        continue
    if line==str(Num)+"\n":
        fnew.write(str(Num-1)+"\n")
        Num+=1
        continue
        
    if ":" in line:
        print(line)
        start = line.split(" --> ")[0]
        end = line.split(" --> ")[1]
        sNew = splitT(start)        
        eNew = splitT(end)
        NewTimeLine = sNew+" --> "+eNew+'\n'
        print(NewTimeLine)
        fnew.write(NewTimeLine)
    else:
        fnew.write(line)

fnew.close()

