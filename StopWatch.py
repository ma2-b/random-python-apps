import tkinter as tk


running = False 
hours, minutes, seconds = 0, 0, 0

def start():
    global running 
    if not running:
        update()
        running = True
    
        
def pause():
    global running 
    if running:
        stop_watch_lable.after_cancel(update_time)
        running = False
        
def reset():
    global running 
    
    pause()

    global hours, minutes, seconds 
    hours, minutes, seconds = 0, 0, 0
    
    stop_watch_lable.config(text="00:00:00")
    
def update():
    global hours, minutes, seconds
    seconds+=1 
    if seconds == 60:
        minutes+=1
        seconds = 0
    
    if minutes == 60:
        hours+=1 
        minutes = 0 
    
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    
    stop_watch_lable.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    
    global update_time
    update_time = stop_watch_lable.after(1000, update)
    
    
    
        

app = tk.Tk()
app.geometry("490x200")
app.title("stopWatch")

stop_watch_lable = tk.Label(text="00:00:00", font=("Arial",70))
stop_watch_lable.pack()

start_button = tk.Button(text="start", height=5, width=7, font=("Arial",20), command=start)
start_button.pack(side=tk.LEFT)
pause_button = tk.Button(text="pause", height=5, width=7, font=("Arial",20), command=pause)
pause_button.pack(side=tk.LEFT)
reset_button = tk.Button(text="reset", height=5, width=7, font=("Arial",20), command=reset)
reset_button.pack(side=tk.LEFT)
quit_button = tk.Button(text="quit", height=5, width=7, font=("Arial",20), command=app.quit)
quit_button.pack(side=tk.LEFT)



app.mainloop()