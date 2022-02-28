import tkinter as tk
from tkinter.ttk import Radiobutton  
file = open("TkInter.txt", "r")
window = tk.Tk()
window.title("Простая тестовая система")
window.geometry("300x300")
right = 0
close = 0
score = 0
false = 0     
def begin():
        global out,proc,false,right,close
        line = file.readline()
        line = line.rstrip()
        close += 1
        if close==1:
            window.destroy()
        else:
            close+=1
        if line!='':
            root = tk.Tk()
            root.geometry('500x200')
            root.title('q.txt')
            q = tk.Label(root, text=line)
            q.pack()
            for i in range (1,4):
                i=str(i)
                line = file.readline()
                line = line.rstrip()
                i=str(i)
                a = tk.Label(root, text=i + ". " +line)
                a.pack()
            ans = tk.Entry(root, width=40)
            x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
            y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
            root.wm_geometry("+%d+%d" % (x, y))
            ans.pack()
            def submit():
                global answer,score,false
                answer = str(ans.get())
                line = file.readline()
                line = line.rstrip()
                if answer != line:
                    print('Вы не справились, правильный ответ:',line)
                    false += 1
                    root.destroy()
                    begin()
                else:
                    print('Правильно, так держать!')
                    score += 1
                    begin()
                    root.destroy()
            sub = tk.Button(root, text="Принять", command=submit)
            sub.pack()  
        else:
            right=score+false
            print("Вы ответили правильно на ", int((score/right)*100), "% вопросов")
            win = tk.Tk()
            win.title("Ваши результаты")
            win.geometry("300x300")
            out = tk.Label(win, text='Правельный ответ '+ str(score)+' вопросов.')
            proc= tk.Label(win, text='Процент правильных ответов =  '+ str(int((score/right)*100))+' %')
            out.pack()
            proc.pack()              
start = tk.Label(window, text="Проверка ваших знаний")
start.pack()
Button = tk.Button(window, command=begin, text="Начать тест")
Button.pack()
end = tk.Button(window, text="Завершить", command=window.destroy)
end.pack()
x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))
window.mainloop()
