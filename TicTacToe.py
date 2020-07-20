# -*- coding: utf-8 -*-
# @Time    : 20-07-2020 06:53 PM
# @Author  : Mohammad Akram
# @Email   : akramtoday@gmail.com

class TicTacToe:
    def __init__(self, dim):
        self.m = dim
        self.board = [[" " for _ in range(dim)] for __ in range(dim)]
    def print(self):
        # for i in range(self.m):
        #     print(" ".join(self.board[i]))
        ans = []
        for i in range(self.m):
            ans.append(" -"*2)
        ans.append("\n")
        for i in range(self.m):
            ans.append("|")
            for j in range(self.m):
                ans.append(" "+self.board[i][j]+" |")
            ans.append("\n")
            if i==self.m-1:
                continue
            ans.append("|")
            for j in range(self.m):
                ans.append(" " + "-" + " |")
            ans.append("\n")
        for i in range(self.m):
            ans.append(" -"*2)
        ans.append("\n")
        print(''.join(ans))


    def move(self, player):
        self.board[player.pos[0]][player.pos[1]]=player.sign
        if self.check_if_won(player):
            player.win_flag= True


    def check_if_won(self, player):
        x, y = player.pos
        sign = player.sign
        row_check, col_check, dia_check = True, True, True
        #for row checking
        for i in range(self.m):
            if self.board[x][i]!=sign and i!=y:
                row_check = False
                break
        #for column checking
        for i in range(self.m):
            if self.board[i][y]!=sign and i!=x:
                col_check = False
                break
        #for diagonal checking
        for i in range(self.m):
            if self.board[i][i]!=sign and i!=x and i!=y:
                dia_check = False
            if self.board[i][self.m-i-1]!=sign and i!=x and self.m-i-1!=y:
                dia_check = False
        return row_check | col_check | dia_check

class Person:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
        self.win_flag = False
    def get_pos(self):
        self.pos = input(self.name+" enter Coodinates: ").split()
        self.pos = [int(x) for x in self.pos]



if __name__ == '__main__':
    t = TicTacToe(3)
    p1= Person(input("Enter Name: "), input("Enter sign: "))
    p2= Person(input("Enter Name: "), input("Enter sign: "))
    t.print()
    #assume p1 will be first
    while(True):
        p1.get_pos()
        t.move(p1)
        t.print()
        if p1.win_flag:
            print(p1.name,"is the winner of the game!!")
            break
        p2.get_pos()
        t.move(p2)
        t.print()
        if p2.win_flag:
            print(p1.name,"is the winner of the game")
            break


