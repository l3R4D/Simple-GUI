import tkinter as tk


class Quiz(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartScreen, QuestionScreen, OptionScreen, EndScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class QuestionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self, text="Question Screen", fg='black', font=('', 60))
        start_button = tk.Button(self, text="Back", fg='black', width=10,
                                 command=lambda: controller.show_frame(StartScreen))
        answer_button = tk.Button(self, text="Answer", fg='black', width=10,
                                  command=lambda: controller.show_frame(EndScreen))

        title_label.pack()
        start_button.pack()
        answer_button.pack()


class StartScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self, text="Start Screen", fg='black', font=('', 60))
        start_button = tk.Button(self, text="Start!", fg='black', width=10,
                                 command=lambda: controller.show_frame(QuestionScreen))
        options_button = tk.Button(self, text="Options", fg='black', width=10,
                                   command=lambda: controller.show_frame(OptionScreen))

        title_label.pack()
        start_button.pack()
        options_button.pack()


class OptionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self, text="Options Screen", fg='black', font=('', 60))
        home_button = tk.Button(self, text="Back", fg='black', width=10,
                                command=lambda: controller.show_frame(StartScreen))

        title_label.pack()
        home_button.pack()


class EndScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self, text="End Screen", fg='black', font=('', 60))
        retry_button = tk.Button(self, text="Retry?", fg='black', width=10,
                                 command=lambda: controller.show_frame(QuestionScreen))

        title_label.pack()
        retry_button.pack()
