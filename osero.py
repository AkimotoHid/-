import tkinter
import tkinter.messagebox
import random

FS = ("Times New Roman", 30)
FL = ("Times New Roman", 80)
BLACK = 1
WHITE = 2
mx = 0
my = 0
mc = 0
proc = 0
turn = 0
msg = ""
space = 0
color = [0]*2
who = ["あなた", "コンピュータ"]
board = []
board2= []
board3= []
for y in range(8):
    board.append([0,0,0,0,0,0,0,0])
for yy in range(8):
    board2.append([0,0,0,0,0,0,0,0])
for yyy in range(8):
    board3.append([0,0,0,0,0,0,0,0])

def click(e):
    global mx, my, mc
    mc = 1
    mx = int(e.x/80)
    my = int(e.y/80)
    if mx>7: mx = 7
    if my>7: my = 7

def banmen():
    cvs.delete("all")
    cvs.create_text(320, 670, text=msg, fill="silver", font=FS)
    for y in range(8):
        for x in range(8):
            X = x*80
            Y = y*80
            cvs.create_rectangle(X, Y, X+80, Y+80, outline="black")
            if board[y][x]==BLACK:
                cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="black", width=0)
            if board[y][x]==WHITE:
                cvs.create_oval(X+10, Y+10, X+70, Y+70, fill="white", width=0)
    cvs.update()

def ban_syokika():
    global space
    space = 60
    for y in range(8):
        for x in range(8):
            board[y][x] = 0
    board[3][4] = BLACK
    board[4][3] = BLACK
    board[3][3] = WHITE
    board[4][4] = WHITE

    for y in range(8):
        for x in range(8):
            board2[y][x] = 0
    board2[3][4] = BLACK
    board2[4][3] = BLACK
    board2[3][3] = WHITE
    board2[4][4] = WHITE

    for y in range(8):
        for x in range(8):
            board3[y][x] = 0
    board3[3][4] = BLACK
    board3[4][3] = BLACK
    board3[3][3] = WHITE
    board3[4][4] = WHITE




# 石を打ち、相手の石をひっくり返す
def ishi_utsu(x, y, iro):
    board[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board[sy][sx]==0:
                    break
                if board[sy][sx]==3-iro:
                    k += 1
                if board[sy][sx]==iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board[sy][sx] = iro
                    break

def ishi_utsu2(x, y, iro):
    board2[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board2[sy][sx]==0:
                    break
                if board2[sy][sx]==3-iro:
                    k += 1
                if board2[sy][sx]==iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board2[sy][sx] = iro
                    break

def ishi_utsu3(x, y, iro):
    board3[y][x] = iro
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board3[sy][sx]==0:
                    break
                if board3[sy][sx]==3-iro:
                    k += 1
                if board3[sy][sx]==iro:
                    for i in range(k):
                        sx -= dx
                        sy -= dy
                        board3[sy][sx] = iro
                    break


# そこに打つといくつ返せるか数える
def kaeseru(x, y, iro):
    if board[y][x]>0:
        return -1 # 置けないマス
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board[sy][sx]==0:
                    break
                if board[sy][sx]==3-iro:
                    k += 1
                if board[sy][sx]==iro:
                    total += k
                    break
    return total

def kaeseru2(x, y, iro):
    if board2[y][x]>0:
        return -1 # 置けないマス
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board2[sy][sx]==0:
                    break
                if board2[sy][sx]==3-iro:
                    k += 1
                if board2[sy][sx]==iro:
                    total += k
                    break
    return total

def kaeseru3(x, y, iro):
    if board3[y][x]>0:
        return -1 # 置けないマス
    total = 0
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            k = 0
            sx = x
            sy = y
            while True:
                sx += dx
                sy += dy
                if sx<0 or sx>7 or sy<0 or sy>7:
                    break
                if board3[sy][sx]==0:
                    break
                if board3[sy][sx]==3-iro:
                    k += 1
                if board3[sy][sx]==iro:
                    total += k
                    break
    return total

# 打てるマスがあるか調べる
def uteru_masu(iro):
    for y in range(8):
        for x in range(8):
            if kaeseru(x, y, iro)>0:
                return True
    return False

# 黒い石、白い石、いくつかあるか数える
def ishino_kazu():
    b = 0
    w = 0
    for y in range(8):
        for x in range(8):
            if board[y][x]==BLACK: b += 1
            if board[y][x]==WHITE: w += 1
    return b, w

def ok(X, Y, iro):
              for dy in range(-1, 2):
                  for dx in range(-1, 2):
                      XXX=0
                      YYY=0
                      sx = X
                      sy = Y
                      while True:
                                 sx += dx
                                 sy += dy
                                 if sx<0 or sx>7 or sy<0 or sy>7:
                                      break
                                 if board[sy][sx]==0:
                                      break
                                 if board[sy][sx]==3-iro:
                                      YYY +=KwoSiraberu(sx, sy)
                                 if board[sy][sx]==iro:
                                      XXX += YYY
                                      break

                                      
              return XXX
                  
def ok2(X, Y, iro):
    for A in range(8):
        for B in range(8):
           board2[A][B]=board[A][B]  
    
    kaihoudo=530000
    ishi_utsu2(X, Y, iro)
    for a in range(8):
        for b in range(8):
            if kaeseru2(a, b, 3-iro)>0:
              if ok3(a, b, iro)<kaihoudo:
                  kaihoudo = ok3(a, b, iro)

    for A in range(8):
        for B in range(8):
           board2[A][B]=board[A][B]  


    return kaihoudo

def ok3(X, Y, iro):
    for dy in range(-1, 2):
                  for dx in range(-1, 2):
                      XXX=0
                      YYY=0
                      sx = X
                      sy = Y
                      while True:
                                 sx += dx
                                 sy += dy
                                 if sx<0 or sx>7 or sy<0 or sy>7:
                                      break
                                 if board2[sy][sx]==0:
                                      break
                                 if board2[sy][sx]==iro:
                                      YYY +=KwoSiraberu2(sx, sy)
                                 if board2[sy][sx]==3-iro:
                                      XXX += YYY
                                      break     
           
    return XXX

def KwoSiraberu(xx, yy):
                for dy in range(-1, 2):
                  for dx in range(-1, 2):
                      kkk=0
                      sx = xx
                      sy = yy
                      while True:
                                 sx += dx
                                 sy += dy
                                 if sx<0 or sx>7 or sy<0 or sy>7:
                                      break
                                 if board[sy][sx]==0:           
                                      kkk+=1
                                      break
                                 if board[sy][sx]!=0:
                                      break
                return kkk


def KwoSiraberu2(xx, yy):
                for dy in range(-1, 2):
                  for dx in range(-1, 2):
                      kkk=0
                      sx = xx
                      sy = yy
                      while True:
                                 sx += dx
                                 sy += dy
                                 if sx<0 or sx>7 or sy<0 or sy>7:
                                      break
                                 if board2[sy][sx]==0:           
                                      kkk+=1
                                      break
                                 if board2[sy][sx]!=0:
                                      break
                return kkk

def yellow(X, Y, iro):
    for A in range(8):
        for B in range(8):
           board3[A][B]=board[A][B] 
    ishi_utsu3(X, Y, iro)
    if(X==0 and Y==1):
        if(board3[1][0]==iro and board3[2][0]==iro and board3[3][0]==iro and board3[4][0]!=3-iro):
            return 1
        else:
            return 0
    elif(X==0 and Y==6):
        if(board3[6][0]==iro and board3[5][0]==iro and board3[4][0]==iro and board3[3][0]!=3-iro):
            return 1
        else:
            return 0
    elif(X==1 and Y==0):
        if(board3[0][1]==iro and board3[0][2]==iro and board3[0][3]==iro and board3[0][4]!=3-iro):
            return 1
        else:
            return 0
    elif(X==6 and Y==0):
        if(board3[0][6]==iro and board3[0][5]==iro and board3[0][4]==iro and board3[0][3]!=3-iro):
            return 1
        else:
            return 0
    elif(X==7 and Y==1):
        if(board3[1][7]==iro and board3[2][7]==iro and board3[3][7]==iro and board3[4][7]!=3-iro):
            return 1
        else:
            return 0
    elif(X==7 and Y==6):
        if(board3[6][7]==iro and board3[5][7]==iro and board3[4][7]==iro and board3[3][7]!=3-iro):
            return 1
        else:
            return 0
    elif(X==6 and Y==7):
        if(board3[7][1]==iro and board3[7][2]==iro and board3[7][3]==iro and board3[7][4]!=3-iro):
            return 1
        else:
            return 0
    elif(X==1 and Y==7):
        if(board3[7][6]==iro and board3[7][5]==iro and board3[7][4]==iro and board3[7][3]!=3-iro):
            return 1
        else:
            return 0
              
def red(X, Y, iro):
    for A in range(8):
        for B in range(8):
           board3[A][B]=board[A][B]
    ishi_utsu3(X, Y, iro)
    if board3[1][1]==iro and board3[6][1]==iro and board3[1][6]==iro and board3[6][6]!=iro:
        return 1
    else:
        return 0

def computer_0(iro):
    kaihoudo=530000

    if kaeseru(0, 0, iro)>0:
        return 0, 0

    if kaeseru(0, 7, iro)>0:
        return 0, 7

    if kaeseru(7, 0, iro)>0:
        return 7, 0

    if kaeseru(7, 7, iro)>0:
        return 7, 7

    for Y in range(8):
        for X in range(8):
            if kaeseru(X, Y, iro)>0:
              if (X==0 and Y==1) or (X==1 and Y==0) or (X==0 and Y==6) or (X==6 and Y==0) or (X==1 and Y==7) or (X==7 and Y==1) or (X==7 and Y==6) or (X==6 and Y==7):
                   if yellow(X, Y, iro)==1:
                          return X, Y
                   else:
                     if (ok(X, Y, iro) - ok2(X, Y, iro)) + 530 < kaihoudo:
                          lastX=X
                          lastY=Y
                          kaihoudo = (ok(X, Y, iro) - ok2(X, Y, iro)) + 530
              elif (X==1 and Y==1) or (X==6 and Y==1) or (X==1 and Y==6) or (X==6 and Y==6):
                   if (ok(X, Y, iro) - ok2(X, Y, iro)) + 5300 <kaihoudo:
                            lastX=X
                            lastY=Y
                            kaihoudo = (ok(X, Y, iro) - ok2(X, Y, iro)) + 5300
              elif red(X,Y,iro)==1:
                  if (ok(X, Y, iro) - ok2(X, Y, iro)) + 530 < kaihoudo:
                          lastX=X
                          lastY=Y
                          kaihoudo = (ok(X, Y, iro) - ok2(X, Y, iro)) + 530
              else:
                   if (ok(X, Y, iro) - ok2(X, Y, iro))<kaihoudo:
                            lastX=X
                            lastY=Y
                            kaihoudo = (ok(X, Y, iro) - ok2(X, Y, iro))

    return lastX, lastY

def main():
    global mc, proc, turn, msg, space
    banmen()
    if proc==0: # タイトル画面
        msg = "先手、後手を選んでください"
        cvs.create_text(320, 200, text="Reversi", fill="gold", font=FL)
        cvs.create_text(160, 440, text="先手(黒)", fill="lime", font=FS)
        cvs.create_text(480, 440, text="後手(白)", fill="lime", font=FS)
        if mc==1: # ウィンドウをクリック
            mc = 0
            if (mx==1 or mx==2) and my==5:
                ban_syokika()
                color[0] = BLACK
                color[1] = WHITE
                turn = 0
                proc = 1
            if (mx==5 or mx==6) and my==5:
                ban_syokika()
                color[0] = WHITE
                color[1] = BLACK
                turn = 1
                proc = 1
    elif proc==1: # どちらの番か表示
        msg = "あなたの番です"
        if turn==1:
            msg = "コンピュータ 考え中."
        proc = 2
    elif proc==2: # 石を打つマスを決める
        if turn==0: # プレイヤー
            if mc==1:
                mc = 0
                if kaeseru(mx, my, color[turn])>0:
                    ishi_utsu(mx, my, color[turn])
                    space -= 1
                    proc = 3
        else: # コンピュータ
            cx, cy = computer_0(color[turn])
            ishi_utsu(cx, cy, color[turn])
            space -= 1
            proc = 3
    elif proc==3: # 打つ番を交代
        msg = ""
        turn = 1-turn
        proc = 4
    elif proc==4: # 打てるマスがあるか
        if space==0:
            proc = 5
        elif uteru_masu(BLACK)==False and uteru_masu(WHITE)==False:
            tkinter.messagebox.showinfo("", "どちらも打てないので終了です")
            proc = 5
        elif uteru_masu(color[turn])==False:
            tkinter.messagebox.showinfo("", who[turn]+"は打てないのでパスです")
            proc = 3
        else:
            proc = 1
    elif proc==5: # 勝敗判定
        b, w = ishino_kazu()
        tkinter.messagebox.showinfo("終了", "黒={}、白={}".format(b, w))
        if (color[0]==BLACK and b>w) or (color[0]==WHITE and w>b):
            tkinter.messagebox.showinfo("", "あなたの勝ち！")
        elif (color[1]==BLACK and b>w) or (color[1]==WHITE and w>b):
            tkinter.messagebox.showinfo("", "コンピュータの勝ち！")
        else:
            tkinter.messagebox.showinfo("", "引き分け")
        proc = 0
    root.after(100, main)

root = tkinter.Tk()
root.title("発展型開放度理論")
root.resizable(False, False)
root.bind("<Button>", click)
cvs = tkinter.Canvas(width=640, height=700, bg="green")
cvs.pack()
root.after(100, main)
root.mainloop()

