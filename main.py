import tkinter
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#FFFFFF"
BLACK = "#000000"
FONT_NAME = "times new roman"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():

  global REPS
  REPS = 0
  window.after_cancel(timer)#Cancels previuos timer
  canvas.itemconfig(timer_text, text="00:00")
  title.config(text = "Timer")
  check_symbols.config(text = "")
  
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():
  global REPS
  REPS += 1

  work_seconds = WORK_MIN*60
  break_seconds = SHORT_BREAK_MIN*60
  long_break_sec = LONG_BREAK_MIN*60

  if REPS % 2 == 0:
    countdown(break_seconds)
    REPS += 1
    title.config(text =  "Break", fg=PINK)
  elif REPS == 8:
    countdown(long_break_sec)
    REPS += 1
    title.config(text =  "Break", fg=RED)
  else: 
    countdown(work_seconds)
    REPS += 1
    title.config(text =  "Work", fg=GREEN)
  
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
  
def countdown(count):
  
  count_minutes = math.floor(count/60) #Math.floor returns largest whole number <= x ie 4.8 = 4
  count_seconds = count % 60
  
  if count_seconds <  10:#Ensures graphics are 5:00 instead of 5:0
    count_seconds = f"0{count_seconds}" #Dynamic typing changing integer tostrign by reseting variable to new value

  canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
  
  if count > 0:
    global timer
    timer = window.after(1000, countdown, count-1) #Method that takes amount of time it should wait in milliseconds then calls particular function after said time
  else:
    timer_start()
    checks = ""
    work_reps = math.floor(REPS/2)
    for i in range(0, work_reps):
      checks+="✔"
    check_symbols.config(text = checks)
    
# ---------------------------- UI SETUP ------------------------------- #

#Window
window = tkinter.Tk()
window.title("POMODORO Application")
window.config(padx=100,pady=200, bg = WHITE) #Adds window space outside image
             
#Title
title = Label(text="timer", fg=BLACK, bg=WHITE, font=(FONT_NAME, 26, "bold"))
title.grid(column=1, row=0)

#Background with Tomato image
canvas = tkinter.Canvas(width=200,height=225, bg = WHITE, highlightthickness=0) #highlightthickness takes canvas border away
tomato_pic = tkinter.PhotoImage(file="tomato.png")# Reads image file
canvas.create_image(100, 100,image=tomato_pic)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="START", command=timer_start)
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET",command=timer_reset)
reset_button.grid(column=2, row=2)

check_symbols = Label(text = "", fg=GREEN, bg=WHITE, font=(FONT_NAME, 20, "bold"))
check_symbols.grid(column=1, row=3)


window.mainloop() #Loops through and checks if something happenend every miliseconds
#*Can't use loops other than this intkinter GUI's
