######!/home/sonikx/Documents/planer/venv/bin/python
#if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
#    os.chdir(sys._MEIPASS)
from tkinter import *
import geocoder
from tkcalendar import Calendar, DateEntry
from tkinter import Label, Tk, ttk
from PIL import Image, ImageTk
import requests
from tkinter import font
# import smtplib
from datetime import timedelta 
from datetime import datetime
# from datetime import *
import os
import time
import inspect
import pygame
import subprocess # для открытия gnome фаиловой систем
import asyncio
import multiprocessing
list_of_buttoms = []
sring_my = """\n\n\n\nHello!\n\nI am called to rescue you from the hellish chaos of life. Where you can define your path, divide it into stages, understand the possibilities of time and your pace. And what is very important, you can see all the work done and admire yourself.\n\nI'll always keep you posted."""
numbers = [(Image.open("Numbers/1_1.png"),Image.open("Numbers/1_2.png")),(Image.open("Numbers/2_1.png"), Image.open("Numbers/2_2.png")), (Image.open("Numbers/3_1.png"),Image.open("Numbers/3_2.png")), (Image.open("Numbers/4_1.png"),Image.open("Numbers/4_2.png")), (Image.open("Numbers/5_1.png"),Image.open("Numbers/5_2.png")), (Image.open("Numbers/6_1.png"),Image.open("Numbers/6_2.png")),(Image.open("Numbers/7_1.png"),Image.open("Numbers/7_2.png")),(Image.open("Numbers/8_1.png"),Image.open("Numbers/8_2.png")), (Image.open("Numbers/9_1.png"),Image.open("Numbers/9_2.png"))]
type_to_image = {
    "programming": Image.open("pc.png"),
    "health": Image.open("m.png"),
    "erudition": Image.open("cr.png"),
    "work": Image.open("money.png"),
    "cleanliness": Image.open("c.png"),
    'switcher': Image.open("aaa1.png")
}
number = 0
curr_date = 0
flags_dict = {(1,0,0):'znak1.png',(0,1,0):'circlered.png',(0,0,1):'translucent-image.png'} #(1,1,0):'',(0,1,1):'',(1,0,1):'',(1,1,1):''

def start_app(var, var1, var3):

    class MyTk(Tk):
        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.x = 0
            self.id = self.after(1000, self.check_touch)
            
        def check_touch(self):
            print('check_touch check_touch check_touch', curr_date)
            if var1.value != 0:
                tkc.selection_set(var1.value)
                kc.selection_set = 0
            
    class Tooltip:
        def __init__(self, widget, text):
            self.widget = widget
            self.text = text
            self.tooltip = None
            self.widget.bind("<Enter>", self.show)
            self.widget.bind("<Leave>", self.hide)

        def show(self, event=None):
            x, y, _, _ = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + 25
            y += self.widget.winfo_rooty() + 25

            self.tooltip = Toplevel(self.widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{x}+{y}")

            label = ttk.Label(
                self.tooltip,
                text=self.text,
                background="white",
                relief="solid",
                borderwidth=0,
            )
            label.pack()

        def hide(self, event=None):
            if self.tooltip:
                self.tooltip.destroy()
                self.tooltip = None


    class ScrollableFrame(ttk.Frame):
        def __init__(self, container, *args, **kwargs):
            super().__init__(container, *args, **kwargs)
            self.canvas = Canvas(self, bg="white")
            self.canvas.pack(fill=BOTH, expand=True)
            scrollbar = Scrollbar(
                self,
                orient="vertical",
                command=self.canvas.yview,
                bg="green",
                bd=0,
                troughcolor="white",
            )
            self.scrollable_frame = Frame(self.canvas, bg="white")

            self.scrollable_frame.bind("<Configure>", self.OnFrameConfigure)

            self.canvas_frame = self.canvas.create_window(
                (0, 0), window=self.scrollable_frame, anchor="nw"
            )
            self.canvas.configure(yscrollcommand=scrollbar.set)
            self.canvas.bind("<Configure>", self.FrameWidth)
            self.canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            root.bind_all("<MouseWheel>", self._on_mousewheel)

        def FrameWidth(self, event):
            canvas_width = event.width
            self.canvas.itemconfig(self.canvas_frame, width=canvas_width)

        def OnFrameConfigure(self, event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        def _on_mousewheel(self, event):
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    def window():
        pass

    def _from_rgb(rgb):
        """translates an rgb tuple of int to a tkinter friendly color code"""
        r, g, b = rgb
        return f"#{r:02x}{g:02x}{b:02x}"


    # Работа с календарем удаление
    def updateLabel(a):
        print('inspect.stack()[1][2] = ', inspect.stack()[1][2])


        list_menus = {}
        if os.stat("settings.txt").st_size > 5:
            get_schedule()
        labelblue.config(text="Selected Date: " + tkc.get_date(), font=85)
        for i in scrollbar.scrollable_frame.winfo_children():  # тут др фрей
            i.destroy()
        #print('1global curr_date = ', curr_date)
        #print('1global curr_date = ', curr_date)
        global curr_date
        curr_date = tkc.get_date()
        with open("date.txt", "w+") as f:
            f.write(curr_date)
        var.value = curr_date
        print('global curr_date = ', curr_date)
        def callBackFunc():  # обновление всех галочек по текущей дате
            print('len(dict_[curr_date]) len(dict_[curr_date]) len(dict_[curr_date]) ',len(dict_[curr_date]))
            if curr_date in dict_ and len(dict_[curr_date])>0:
                print('callBackFunc start!!!!!!!!!!!!!')
                n = 0
                date_progress = 0
                print("dict_for_variables", dict_for_variables)
                for i in range(len(dict_[curr_date])):
                    dict_[curr_date][n][-1] = dict_for_variables[curr_date][
                        n
                    ].get()
                    print()
                    date_progress += dict_[curr_date][n][-1]*100/len(dict_[curr_date])
                    n += 1

                def update_progressbar():
                    k = 0
                    while k <= date_progress:
                    ### some work to be done
                        percetage_progress.set(k)
                        k += 1
                        time.sleep(0.012)
                        root.update_idletasks()
                    #root.after(100, update_progressbar)
                update_progressbar() 
        
        dict_for_variables = {}
        if curr_date in data_flags_dict:
            print( 'if curr_date in data_flags_dict',  curr_date in data_flags_dict)
            curr_frame_FLAG = Frame(
                        scrollbar.scrollable_frame,
                        background="#FF8000",
                        borderwidth=2,
                        highlightthickness=2,
                        bd=2,
                        relief="groove", 
                    )
            curr_frame_FLAG.pack(side="top", fill=X)
            print( data_flags_dict[curr_date])
            T = Label(curr_frame_FLAG, text=data_flags_dict[curr_date][-1], background="white", font=("Arial", 12, "bold"))
            T.pack(side="top", fill=X)
            #T.insert(tk.END, Fact)
        if curr_date in dict_:
            for i in range(len(dict_[curr_date])):
                dict_for_variables[curr_date] = dict_for_variables.get(
                    curr_date, []
                ) + [IntVar()]
                dict_for_variables[curr_date][i].set(dict_[curr_date][i][-1])
                list_menus[curr_date] = list_menus.get(curr_date, []) + [
                    [IntVar(), IntVar()]
                ]
            

            for i in range(len(dict_[curr_date])):  # восстановление окна с задачами
                #progress_state += dict_[curr_date][-1]
                dict_[curr_date]= list(sorted(dict_[curr_date], key=lambda x:x[2])) #SORT
                current_task = dict_[curr_date][i][0]
                curr_frame = Frame(
                    scrollbar.scrollable_frame,
                    background="white",
                    borderwidth=0,
                    highlightthickness=0,
                    bd=0,

                )
                #progressbar
                curr_frame.pack(side="top", fill=X)

 
         
                frame_for_number = Frame(curr_frame, width=26, height=20, bg='white')
                frame_for_number.pack(side="left")
                number_of_task = i+1
                def lab_top(*args):
                    print('lab_top - args=',  args[0].widget)
                    number = str(args[0].widget).split('.')[-3]
                    print('number==', number, number.isdigit())
                    if any(ch.isdigit() for ch in number): number = int(number[-1])
                    else:
                        number = 1
                    dict_[curr_date][number-1][2] = number-1
                    dict_[curr_date][number - 2][2] = number
                    updateLabel('a')
                def lab_down(*args):
                    print('down')
                    dict_[stroka][1] = dict_[stroka][1] - 1
                    updateLabel('a')
                    print(dict_[stroka])

                img1, img2 = numbers[i][0], numbers[i][1]
                resized_image1, resized_image2 = img1.resize((22, 10)), img2.resize((22, 10))
                photo1 = ImageTk.PhotoImage(resized_image1)
                photo2 = ImageTk.PhotoImage(resized_image2)
                laby_top = Label(frame_for_number, image=photo1,bd='0.14m')
                laby_down = Label(frame_for_number, image=photo2,bd='0.1m')
                #list_of_buttoms.append(laby_top) #когда цикл создания окончен к кажой кнопке задается ее номер

                laby_top.image = photo1
                laby_down.image = photo2
                laby_top.pack(side="top")
                laby_down.pack(side="bottom")
                #print('laby_top=',laby_top)
                laby_top.bind("<Button-1>", lab_top)
                laby_down.bind("<Button-1>", lab_down)

                current_task = Checkbutton(
                    curr_frame,
                    text=current_task,
                    font=45,
                    bg="white",
                    variable=dict_for_variables[curr_date][i],
                    onvalue=1,
                    offvalue=0,
                    highlightthickness=0,
                    bd=0,
                    
                )  

                def delete():
                    for i in range(len(list_menus[curr_date])):
                        if list_menus[curr_date][i][0].get() == 1:
                            # del list_menus[curr_date][i]
                            del dict_[curr_date][i]
                            scrollbar.scrollable_frame.winfo_children()[
                                i
                            ].destroy()
                    updateLabel('a')

                menubutton = Menubutton(curr_frame, text="...", bg="white")
                menubutton.menu = Menu(menubutton)
                menubutton["menu"] = menubutton.menu
                deletebtn = menubutton.menu.add_checkbutton(
                    label="Delete",
                    variable=list_menus[curr_date][i][0],
                    command=delete,
                )
                # deletebtn.bind(<>,)
                # print('deletebtn type is', type(deletebtn))
                # editbtn = menubutton.menu.add_checkbutton(label = "Edit",
                #   variable = list_menus[curr_date][i][1])

                def description(event):
                    numb = 0
                    for curr_frame in scrollbar.scrollable_frame.winfo_children():
                        for widget in curr_frame.winfo_children():
                            if event.widget == widget:
                                result_numb = numb
                        numb += 1

                    Tooltip(event.widget, dict_[curr_date][result_numb][-2])

                current_task.bind("<Enter>", description)
                # current_task.bind("<Leave>", lambda event: event.widget.config(bg="white", fg="navy"))

                # print('current_task.cget("text")',current_task.cget("text"))
                current_task["command"] = callBackFunc
                # print('dict_[curr_date][i]', dict_[curr_date][i] )
                print()
                # dict_[curr_date][i][-1] = eval(a).get()
                # print(dict_)
                current_task.pack(side="left")
                # print(dict_)
                # Image.open('mass.png')
                img = type_to_image[dict_[curr_date][i][1]]
                resized_image = img.resize((30, 30))
                photo = ImageTk.PhotoImage(resized_image)
                lab = Label(curr_frame, image=photo)
                lab.image = photo
                lab.pack(side="right")
                menubutton.pack(side="right")
                print('inspect.stack()[1][2] = ', inspect.stack()[1][2])
            if inspect.stack()[1][3] in ['delete', 'fetch'] or  inspect.stack()[1][2] in [789, 827, 1948]: #если функция вызвана из функций добавления, удаления, отметки задачь, то вызываем callBackFunc()
                callBackFunc() 
        #print('list_of_buttoms=',list_of_buttoms)
    # first run
    def hello():
        global tkc
        hello = Toplevel(root)
        root["bg"] = "white"
        hello.title("Hellper_2.0")
        hello.geometry("1000x480")
        # hello.eval('tk::PlaceWindow . center')
        frame1 = Frame(hello, bg="white", width=200, height=200)
        frame1.pack(fill=BOTH, expand=True, side="left")
        frame2 = Frame(hello, bg="white", width=200, height=200, background='red')
        frame2.pack(fill=BOTH, expand=True, side="left")
        global icon1
        # photo = ImageTk.PhotoImage(image)
        Label(frame1, image=icon1, bg="white").pack(
            fill=BOTH, expand=True, padx=12
        )
        global my_font
        noteditor = Text(
            frame2,
            wrap="word",
            bg="white",
            font=my_font,
            highlightthickness=0,
            borderwidth=0,
            height=14,
        )
        noteditor.pack(fill=BOTH, expand=1, padx=35)
        # noteditor.insert(5.5, 'Hello!')
        global sring_my
        noteditor.insert(7.0, sring_my)
        noteditor.config(state=DISABLED)

        def open_settings():
            global tkc
            hello.withdraw()
            settings_window()

        frame3 = Frame(frame2, bg="green", width=200, height=100)
        frame3.pack(fill=BOTH, expand=True, side="bottom")
        global my_font2
        btn = Button(
            frame3,
            bg="white",
            text="start settings",
            font=my_font2,
            foreground="red",
            justify=RIGHT,
            command=open_settings,
            highlightthickness=0,
            borderwidth=0,
        )
        btn.configure(width=200, height=100)
        btn.pack(anchor="se")


    def get_schedule(
        *A,
    ):  # работа над заполнением рабочих дней функция проставляет даты рабочих дней при загрузке
        with open("settings.txt") as fe:
            # print('fe.read()',fe.read(), 'type(fe.read()) = = ', type(fe.read()))
            print(
                'os.stat("settings.txt").st_size ', os.stat("settings.txt").st_size
            )
            if os.stat("settings.txt").st_size > 5:
                text = fe.read()
                print("text = ", text)
                settings_list = eval(text)
            else:
                settings_list = []
            # print('settings_list',settings_list)
        # удаляет все события календары. можно указать список необходимых к удаленю
        tkc.calevent_remove()
        print("settings_list ==", settings_list)
        date = datetime(*map(int, settings_list[3].split("-")))
        selected = settings_list[2]
        # print('selected', selected)
        date_last = date + timedelta(days=int(selected.split("/")[-1]) + 1)
        #  if list_of_workdays:
        #     tkc.calevent_remove(*list_of_workdays)
        step = int(selected.split("/")[-1])
        # step_weekend = int(selected.split('/')[0])-1
        # последний введеный выходной день
        for i in range(130):
            for j in range(int(selected.split("/")[0])):
                # print('date_last', date_last)
                work_event = tkc.calevent_create(
                    date=date_last, text="WorkDay", tags="tag"
                )
                tkc.tag_config(
                    "tag", background="azure2", foreground="dodgerblue4"
                )
                # list_of_workdays.append(work_event)
                date_last = date_last + timedelta(days=1)
            date_last = date_last + timedelta(days=step)
        # frame.update()
        # root.update()
        tkc.update()


    # settings window
    def settings_window():
        global tkc
        settings.deiconify()
        frame1 = Frame(settings, bg="white")
        frame1.pack()
        title = Label(
            frame1,
            text="Settings",
            font=my_font2,
            bg="white",
            highlightthickness=0,
            bd=0,
            pady=15,
        ).pack()
        frame_email = Frame(settings, bg="white", width=200, height=100)
        frame_email.pack(fill=BOTH, expand=True)
        title = Label(
            frame_email,
            text="Enter your mail: ",
            font=my_font,
            bg="white",
            highlightthickness=0,
            bd=0,
            pady=15,
        ).pack(side=LEFT, fill=X)
        entry1 = Entry(frame_email, width=30)
        entry1.pack(side=LEFT, fill=X)
        frame_name = Frame(settings, bg="white", width=200, height=100)
        frame_name.pack(fill=BOTH, expand=True)

        entry2 = Entry(frame_name, width=30)
        entry2.pack(side=LEFT, fill=X)
        frame_work = Frame(settings, bg="white", width=200, height=100)
        frame_work.pack(fill=BOTH, expand=True)

        # frame_worktime = Frame(settings, bg='white', width=200, height=100).pack(side=LEFT, fill = X).pack()
        counter = 0

        def select(selected):
            nonlocal counter
            counter += 1
            if counter > 1:
                frame_worktime.destroy()
            frame_worktime = Frame(settings, bg="white", width=200, height=100)
            frame_worktime.pack(side=LEFT, fill=X)
            #        title = Label(
            #           frame_worktime,
            #          text="Set your worktime (08:00 20:00): ",
            #         font=my_font,
            #        bg="white",
            #       highlightthickness=0,
            #      bd=0,
            #     pady=15,
            # ).pack(side=LEFT, fill=X)
            entry_start = Entry(frame_worktime)
            entry_start.pack(side=LEFT, fill=X)
            entry_end = Entry(frame_worktime)
            entry_end.pack(side=LEFT, fill=X)
            #        title = Label(
            #           frame_worktime,
            #          text="Last workday: ",
            #          font=my_font,
            #          bg="white",
            #          highlightthickness=0,
            #          bd=0,
            #          pady=15,
            #      ).pack(side=LEFT, fill=X)
            datentry = DateEntry(frame_worktime)
            datentry.pack(side=LEFT, fill=X)

            def saving_and_destroy():
                settings_list = [
                    entry1.get(),
                    entry2.get(),
                    btn.get(),
                    str(datentry.get_date()),
                    entry_start.get(),
                    entry_end.get(),
                ]
                with open("settings.txt", mode="w") as f:
                    f.write(str(settings_list))
                get_schedule()
                settings.withdraw()
                updateLabel("a")
                root.deiconify()

        btn = StringVar()

        def f():
            selected = btn.get()
            select(selected)

        list_ = ["5/2", "1/3", "2/2"]
        for schedule in list_:
            schedule = Radiobutton(
                frame_work,
                text=schedule,
                value=schedule,
                variable=btn,
                command=f,
                bg="white",
            )
            schedule.pack(side=LEFT, fill=X)


    #switch


    def func():  # Определяет геолокацию и погоду
        BASE_URL = "https://api.open-meteo.com/v1/forecast"
        g = geocoder.ip("me")
        city = g.latlng
        # Параметры запроса для Краснодара
        params = {
            "latitude": city[0],  # широта Краснодара
            "longitude": city[1],  # долгота Краснодара
            # минимальная и максимальная температура, сумма осадков
            "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum",
            "timezone": "Europe/Moscow",
        }  # временная зона для Краснодара
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        user_name["text"] = (
            str(g.city) + " : " + str(data["daily"]["temperature_2m_max"][1])
        )


    flags = (0,0,0)

    def func1():
        stroka = tkc.get_date()

        newWindow = Toplevel(root)
        newWindow.title("Add your task/goal")
        newWindow.geometry("700x300")
        newWindow.attributes('-topmost', 1)
        class_tasks = ["Goal", "Task", "Day"]
        combobox = ttk.Combobox(newWindow, values=class_tasks)
        combobox.pack()
        combobox.insert(0, "Task")

        def goal_or_task(a, b=False):
            def fetch():
                if temporary == 'Day':
                    print("Variable x exists")
                    nonlocal flags
                    nonlocal data_flags_dict
                    flags = (varr1.get(), varr2.get(), varr3.get())
                    print('flags = ', flags)
                    if flags != (0,0,0):
                        var3.value = flags_dict[flags] # отправляем сигнал pyqt с названием фото и он по дате определяет ячейку и ставить фото
                        with  open('tkc_flags.txt', "w+") as h: # для передачи qt

                            data_flags_dict[curr_date] = (flags_dict[flags], max([editor_d1.get(1.0, END),editor_d2.get(1.0, END),editor_d3.get(1.0, END)], key=len))
                            h.write(str(data_flags_dict))
                        flags = (0,0,0)
                        
                elif temporary == 'Task' and combobox1.get():
                    if tasky.get():

                        task_name, task_type = tasky.get(), combobox1.get()
                        global number
                        numb = len(dict_.get(stroka, '1'))   # номер задачи
                        dict_[stroka] = dict_.get(stroka, []) + [
                            [task_name,  task_type,numb, editor.get(1.0, END), False]  #формат заполнения your_story
                        ]
                        number += 1
                        updateLabel('a')
                        try:
                            print('dict_ befo record =', dict_)
                            record('fetch')
                        except: sys.exit("Не могу записать файл!")
                newWindow.destroy()
            if combobox.get() == "Day":
                temporary = "Day"
                newWindow.geometry("980x300")
                for i in newWindow.winfo_children()[1:]:  # тут др фрейм
                    i.destroy()

                newWindow.update()
                varr1, varr2, varr3 = IntVar(), IntVar(), IntVar()
                frameall = Frame(newWindow, background="white")
                frameall.pack(fill=BOTH, expand=True)
                framegv = Frame(frameall, background="red")
                framegv.pack(side=LEFT, fill=BOTH, expand=True)
                frame11 = Frame(framegv, background="blue")
                frame11.pack(side=LEFT,fill=BOTH, expand=True)
                frame12 = Frame(framegv, background="green")
                frame12.pack(side=LEFT,fill=BOTH, expand=True)
                frame13 = Frame(framegv, background="yellow")
                frame13.pack(side=LEFT,fill=BOTH, expand=True)
                c1 = Checkbutton(frame11, text='exclamation mark',variable=varr1, onvalue=1, offvalue=0, )
                c1.pack(side=LEFT, fill=BOTH)
                editor_d1 = Text(
                    frame11,
                    width=25,
                    height=5,
                    bg="darkgreen",
                    fg="white",
                    wrap=WORD,
                )
                editor_d1.pack(fill=BOTH, expand=1)
                c2 = Checkbutton(frame12, text='encircle',variable=varr2, onvalue=1, offvalue=0, )
                c2.pack(side=LEFT, fill=BOTH)
                editor_d2 = Text(
                    frame12,
                    width=25,
                    height=5,
                    bg="darkgreen",
                    fg="white",
                    wrap=WORD,
                )
                editor_d2.pack(fill=BOTH,)
                c3 = Checkbutton(frame13, text='check mark',variable=varr3, onvalue=1, offvalue=0, )
                c3.pack(side=LEFT, fill=BOTH)
                editor_d3 = Text(
                    frame13,
                    width=25,
                    height=5,
                    bg="darkgreen",
                    fg="white",
                    wrap=WORD,
                )
                editor_d3.pack(fill=BOTH, expand=1)
                b = Button(newWindow, text="add falgs", command=fetch)
                b.pack(anchor="se")
        
            if combobox.get() == "Task":
                temporary = "Task"
                for i in newWindow.winfo_children()[1:]:  # тут др фрейм
                    i.destroy()

                newWindow.update()
                frameall = Frame(newWindow, background="white")
                frameall.pack(fill=BOTH, expand=True)
                framegv = Frame(frameall, background="white")
                framegv.pack(side=LEFT, fill=BOTH, expand=True)
                frame11 = Frame(framegv, background="white")
                frame11.pack(fill=BOTH, expand=True)
                taskname = Label(frame11, text="Set the task", bg="white")
                taskname.pack(side=LEFT, fill=BOTH)
                tasky = Entry(frame11, width=35)
                tasky.pack(side=LEFT)
                frame22 = Frame(framegv, background="white")
                frame22.pack(fill=BOTH, expand=True)
                frame33 = Frame(frameall, background="white")
                frame33.pack(side=RIGHT, fill=BOTH, expand=True)
                task_description = Label(
                    frame33, text="Task_description", bg="white"
                )
                task_description.pack(side=TOP, fill=X)
                editor = Text(
                    frame33,
                    width=25,
                    height=5,
                    bg="darkgreen",
                    fg="white",
                    wrap=WORD,
                )
                editor.pack(fill=BOTH, expand=1)
                # print('!!!!!!!!!!!!!!!!!!!!!!!!',frame22 )
                types_of_tasks = Label(frame22, text="Set the type", bg="white")
                types_of_tasks.pack(side=LEFT, fill=BOTH)
                # tasky.bind('<Return>', fetch)
                tasks_types = [
                    "programming",
                    "health",
                    "erudition",
                    "work",
                    "cleanliness",
                ]
                combobox1 = ttk.Combobox(
                    frame22, values=tasks_types, background="white"
                )
                combobox1.pack(side=LEFT)
                b = Button(newWindow, text="add task", command=fetch)
                b.pack(anchor="se")
                #newWindow.protocol(
                #   "WM_DELETE_WINDOW", updateLabel("a")
                #)  # close window trigger
            elif combobox.get() == "Goal":
                newWindow.update()

        goal_or_task("a", b=True)

        combobox.bind("<<ComboboxSelected>>", goal_or_task)



    def record(where_is_func):
        print('CLOSE ROOT inspect.stack()[1][2] = ', inspect.stack()[1][2])
        if inspect.stack()[1][2] == 708:
            global stop_async
            stop_async = True
        with open("your_story.txt", "w") as f:
            data = str(dict_)
            print('data', data)
            f.write(data)
            if where_is_func == 'protocol':
                root.destroy()

    def read_dict():
        print('os.stat("settings.txt").st_size ', os.stat("settings.txt").st_size)
        isempty = os.stat("your_story.txt").st_size
        print("isempty", isempty)
        if isempty != 0:
            with open("your_story.txt") as f, open('tkc_flags.txt', "r+") as h:
                nonlocal dict_
                nonlocal data_flags_dict
                dict_ = eval(f.readlines()[0])
                if os.stat("tkc_flags.txt").st_size != 0:
                    print('reading data_flags_dict = ', data_flags_dict)
                    data_flags_dict = eval(h.readlines()[0])
            
    def open_files():
        current_path = os.path.dirname(os.path.abspath(sys.argv[0])) + '/_internal/files' 
        subprocess.run(['xdg-open', current_path])



    
    position = 0
    dict_ = {}
    data_flags_dict = {}
    read_dict()
    
    root = Tk(className='Hellper')
    root.title("Hellper_2.0")
    root["bg"] = "#fafafa"
    #root.attributes('-topmost', 1)
    root.resizable(width=False, height=False)
    icon = PhotoImage(file="aaa.png")
    icon1 = PhotoImage(file="bb.png")
    root.iconphoto(True, icon)
    root.geometry('980x400-700+200')
    # root.eval('tk::PlaceWindow . center')
    root.wm_attributes("-alpha", 0.7)
    # create settings window:
    settings = Toplevel(root)
    root["bg"] = "white"
    settings.title("Hellper_2.0")
    settings.geometry("1000x480")
    root.protocol("WM_DELETE_WINDOW", lambda x='protocol': record(x))


    root.wm_withdraw()  # скрываем окно до окончания настройки

    settings.wm_withdraw()  # скрываем окно до окончания настройки
    my_font2 = font.Font(family="Arial", size=17, weight="bold")
    my_font = font.Font(family="Arial", size=17, weight="normal")
    if os.stat("settings.txt").st_size < 5:
        hello()
    else:
        root.deiconify()
    frame = Frame(root, bg="white", width=200, height=200)
    frame.pack(fill=BOTH, expand=True, side=RIGHT)

    current_font = font.Font(weight="bold", size=13)


    dt_now = str(datetime.now()).split()[0].split("-")
    tkc = Calendar(
        frame,
        selectmode="day",
        year=int(dt_now[0]),
        month=int(dt_now[1]),
        date=int(dt_now[2]),
        foreground="darkorange1",
        font=current_font,
        background="white",
        bordercolor="azure2",
        headersbackground="white",
        weekendbackground="white",
        othermonthbackground="floralwhite",
        weekendforeground="black",
        othermonthwebackground="floralwhite",
        showweeknumbers=False,
        day=int(dt_now[2]),
        disabledselectbackground="yellow",
        disabledselectforeground="blue",
        disableddaybackground="pink",
        selectbackground="green",
    )
    tkc.pack(fill="both", expand=True, padx=17, pady=4)
    #tkc.update()
    tkc_h =  tkc.winfo_height()
    tkc_w = tkc.winfo_width() 
    print('tkc_w', tkc_w, tkc_h)
    tkc.bind("<<CalendarSelected>>", updateLabel)  # нажатие на дату

        

    frame1 = Frame(root, bg="white", width=200, height=200)
    # frame.configure(width=520, height=500)
    frame1.pack(fill=BOTH, expand=True, side=RIGHT)
    percetage_progress = DoubleVar()
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='white', background='#4F4BBF',borderwidth=0,bordercolor='#4F4BBF', darkcolor='#4F4BBF', pbarrelief='groove', thickness=10, troughcolor = 'white')
    progressbar =  ttk.Progressbar(frame1, style="red.Horizontal.TProgressbar", orient="horizontal", variable=percetage_progress)
    progressbar.pack(side="bottom", fill=X, padx=35, pady=9)

    frame4 = Frame(frame1, bg="white")
    frame4.pack(side="top", fill=X)
    frame3 = Frame(frame1, bg="white")
    frame3.pack(side=TOP, fill=BOTH, expand=True)
    scrollbar = ScrollableFrame(frame3)
    scrollbar.pack(fill=BOTH, expand=True)
    btn1 = Button(frame4, text="ADD", bg="white", command=func1)
    btn1.pack(side=LEFT)
    labelblue = Label(frame4, text="Selected Date: ", font=40, bg="white")
    labelblue.pack(side=LEFT)
    image_file = Image.open("folder.jpg")
    resized_image_file = image_file.resize((28, 28))
    photo_file = ImageTk.PhotoImage(resized_image_file)
    btn2 = Button(frame4, text="", bg="white",image=photo_file,borderwidth=0,fg = 'white', highlightthickness=0, command=open_files)
    btn2.pack(padx=13,side=RIGHT)
    labelblue.config(text="Selected Date: " + tkc.get_date(), font=85)


    # Для погоды по геолокации
    image = Image.open("picture.png")
    resized_image = image.resize((28, 28))
    photo = ImageTk.PhotoImage(resized_image)

    # фрейм с погодой
    frame2 = Frame(frame, bg="white", width=100, height=100)
    frame2.pack(side="bottom", fill=X, pady=13)

    # кнопка с фото
    # title = Label(frame2, bg='white')
    btn = Button(
        frame2, text="Создать задачу", bg="white", image=photo, highlightthickness=0,borderwidth=0,fg = 'white', command=func
    )
    btn.configure(width=28, height=28)
    btn.pack(side=LEFT, padx=21, pady=1)
    # title.pack(side='left')
    user_name = Label(
        frame2, text="wheather", font=25, bg="white", highlightthickness=0, bd=0
    )
    user_name.pack(side=LEFT)
    btn_timer = Button(
        frame2, text="timer", font="Arial 13 bold", bg="white", #command=timerr
    )
    btn_timer.pack(side=LEFT, padx=9)
    btn_window = Button(
        frame2, text="window", font="Arial 13 bold", bg="white", command=window
    )
    btn_window.pack(side=LEFT, padx=9)
    btn.invoke()  # кнопка погоды нажатие
    print("cick")

    print('updateLabel ready')
    updateLabel("a") # внимание номер строки! для корректного назала работы приложения (прогрессбар)
    def check_touch():
        print('check_touch check_touch check_touch', curr_date)
        if var1.value != 0:
            tkc.selection_set(var1.value)
            var1.value = 0
            updateLabel("a")
        root.after(1000, check_touch) 
            
    #root.after(1000, check_touch)  # вызываем функцию my_function каждую секунду
    #asyncio.run(check_touch())
    check_touch()
    root.mainloop()
    
stop_async = False

# task coroutine
def check_cell_info(var, var1):
    # report a message
    print('Task check_cell_info starting')
    while True:
        time.sleep(1)
        size = os.path.getsize('check_cell_info.txt')
        print('check_cell_info.txt ========= ', size)
        if size != 0:
            with open('check_cell_info.txt', 'r+') as f:
                f.seek(0)  # move back to the beginning of the file
                cell_number = f.read()
                print('cell_number = ', cell_number)
                os.ftruncate(f.fileno(), 0)  # truncate the file
                f.flush()  # force write to disk
                os.fsync(f.fileno())  # force flush and sync
                f.seek(0)  # move back to the beginning of the file again
                print('size = ', os.path.getsize('check_cell_info.txt'))
            print('var.value = !',str(var.value))
            curr_date = str(var.value).split('/')
            print('curr_date = !', curr_date)
            if len(curr_date[0]) == 1:
                curr_month = int('0'+curr_date[0])
            else: curr_month = int(curr_date[0])
            print('curr_month = !', curr_month)
            curr_year = int(str(20) + curr_date[-1])
            print('curr_year = ', curr_year)
            #c_date = [int(i) for i in data.split('/')]
            #print('TTT')
            print(curr_year, curr_month, 1)
            date_obj = datetime(curr_year, curr_month, 1) #да QT mousePressEvent()
            print('date_obj = ',date_obj)
            day_to_add = int(date_obj.strftime("%w")) -1
            print('day_to_add = ', day_to_add)
            print('cell_number.split("")[-2]) = ', str(cell_number)) #.split("'")[-2].split("'")[-2]
            _date = int(str(cell_number))  #.split("'")[-2])-day_to_add  
            print('date_obj.month ', str(_date)+'/'+str(date_obj.month)+'/'+str(date_obj.year))
            date_result = datetime.strptime(str(_date)+'/'+str(date_obj.month)+'/'+str(date_obj.year), "%d/%m/%Y")
            print('date_result = !!!!!!!!!!!!!!!!!!!!!!!!!!! ', date_result)
            var1.value = date_result
            # 
        print('TYT')       
        #return cell_number

import multiprocessing

import schedule

import multiprocessing
import queue


import threading
# main coroutine





if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        shared_var = manager.Value('i', 0)  # создаем переменную shared_var типа int
        shared_var2 = manager.Value('i', 0)  # создаем переменную shared_var типа int
        shared_var3 = manager.Value('i', 0) # фото
        with multiprocessing.Pool(processes=2) as pool:
            pool.apply_async(start_app, args=(shared_var,shared_var2, shared_var3))
            time.sleep(2)
            pool.apply_async(check_cell_info, args=(shared_var,shared_var2))
            
           
            pool.close()
            pool.join()
          # выводим значение shared_var

# run the asyncio program

#start_app()
