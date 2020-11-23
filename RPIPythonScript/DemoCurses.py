# -*- coding: utf-8 -*-
"""
Created on Fri Nov 01 16:49:42 2019


pip install windows-curses

@author: alt-monneyf
"""

import curses
import time
from curses.textpad import Textbox,rectangle




def CallMenu0(stdscr):
    for i in range(10):
        stdscr.addstr(6,10, "Compteur: {}".format(i/10.0))
        stdscr.clrtoeol()
        stdscr.refresh()
        time.sleep(0.1)
    stdscr.addstr(6,10, "")
    stdscr.clrtoeol()

def PrintMenu(stdscr):
    stdscr.addstr(curses.LINES-1,30, "Press 'q' to quit")
    timeValue = time.time()
    stdscr.addstr(curses.LINES-1, 2, time.ctime(timeValue))
    stdscr.addstr(0,10, "0: Reset Board")
    stdscr.addstr(1,10, "1: Read  memory bank EL502")

def CheckKey(stdscr,key):
    txtToPrint="Selection: "
    stdscr.addstr(5,10, txtToPrint)
    if(key > 0):
        stdscr.addstr(5,10 + len(txtToPrint), "{}".format(chr(key)))
        stdscr.clrtoeol()
        stdscr.refresh()
        if(chr(key)=='0'):
            CallMenu0(stdscr)
            
        time.sleep(0.5)
        stdscr.addstr(5,10 + len(txtToPrint), " ")
        stdscr.clrtoeol()



def main(win):
    #global stdscr
    stdscr = win
    stdscr.nodelay(1)
    stdscr.timeout(0)
    screen_size_ok = True
    try:
        lineMaxPos = 29
        stdscr.addstr(lineMaxPos,0, " ")
    except:
        screen_size_ok = False
    
    if (screen_size_ok):
        key = 0
        while(key != ord('q')):
            
            PrintMenu(stdscr)
            CheckKey(stdscr,key)

            stdscr.refresh()
            key = stdscr.getch()
            
        curses.endwin()
    else:
        curses.endwin()
        print("Screen to small...Maximum number of line: {}".format(curses.LINES-1))
        print("Set the terminal windows bigger...")
    print("End of Test Curses")
#if __name__ == '__main__':
curses.wrapper(main)
