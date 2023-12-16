import eel
import os; from subprocess import *; from time import *; from sys import *; from pathlib import *
import tkinter as tk; from tkinter import *; from tkinter import messagebox 


directory_txt = ('C:\\multiServer\\directory.txt')
try: infile = open(directory_txt, 'r')
except Exception: cErrorT = (directory_txt); cError = ('MissingFile')



