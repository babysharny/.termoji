#!/usr/bin/python
# -*- coding: utf-8 -*-

import random, os, getpass

class text(str):
  
  _colors = ['\033['+str(c)+'m' for c in (list(range(31, 36))+list(range(91, 96)))]

  def color(self, clearEnds=True):
    clear = '\033[0m'
    if not clearEnds: clear=''
    # colors = ['\033['+str(c)+'m' for c in (range(31, 36)+range(90, 97))]
    return text(random.choice(self._colors) + self + clear)
  
  def bold(self):
    clear = '\033[0m'
    bld = '\033[1m'
    return text(bld + self + clear)


def randomSmile():
  abspath = os.path.abspath(__file__)
  dname = os.path.dirname(abspath)
  os.chdir(dname)
  # os.chdir(r'./')
  return random.choice([str(line.strip('\n')) for line in open('kaomoji') if len(line.strip()) > 0])

def splitter():
  rows, columns = os.popen('stty size', 'r').read().split()
  
  line = " -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -  - -"
  # int cols = int(columns)
  return line[0:int(float(columns))]

def ps1():

    line = '\n' + splitter() + '\n'
    line = text(line).color().bold()
    title = text(' '+os.getcwd()).color()
    title += text(r' as '+getpass.getuser()+'\n').color()
    title = text(title).bold()
    input_arrow = ' ' + text(randomSmile()).color().bold() + ' '
    res = line + title + str(input_arrow) + text().color(False)
    # print(res)
    return res

def allColors():
  for color in text()._colors:
    print color + '### WARNING ### ERROR ### FAIL ### DONE! ### OK ###'

exit(ps1())