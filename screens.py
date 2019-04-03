import tkinter as tk
import random

from utils import Fonts


def questions(container, question, answer1, answer2, answer3, answer4, right_command, wrong_command):
    question_label = tk.Label(container, text=question, fg='black', font=Fonts.HEADER.value)
    answer_button1 = tk.Button(container, text=answer1, fg='black', width=10, pady=10,
                               command=right_command)
    answer_button2 = tk.Button(container, text=answer2, fg='black', width=10, pady=10,
                               command=wrong_command)
    answer_button3 = tk.Button(container, text=answer3, fg='black', width=10, pady=10,
                               command=wrong_command)
    answer_button4 = tk.Button(container, text=answer4, fg='black', width=10, pady=10,
                               command=wrong_command)

    buttons = [answer_button1, answer_button2, answer_button3, answer_button4]
    packed_buttons = []
    selector = random.randint(0, len(buttons) - 1)

    question_label.pack()

    for button in buttons:
        while selector in packed_buttons:
            selector = random.randint(0, len(buttons) - 1)
        buttons[selector].pack()
        packed_buttons.append(selector)
        selector = random.randint(0, len(buttons) - 1)


class Quiz(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartScreen, QuestionScreen1, OptionScreen, EndScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class QuestionScreen1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        questions(self, "What is a bee?", "Animal", "Plant", "Chemical", "Insect",
                  lambda: controller.show_frame(StartScreen), lambda: controller.show_frame(EndScreen))

        back_button = tk.Button(self, text="Back", fg='black', width=10,
                                command=lambda: controller.show_frame(StartScreen))
        back_button.pack(side=tk.BOTTOM)


class StartScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self, text="Start Screen", fg='black', font=Fonts.HEADER.value)
        start_button = tk.Button(self, text="Start!", fg='black', width=10,
                                 command=lambda: controller.show_frame(QuestionScreen1))
        options_button = tk.Button(self, text="Options", fg='black', width=10,
                                   command=lambda: controller.show_frame(OptionScreen))

        title_label.pack()
        start_button.pack()
        options_button.pack()


class OptionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self, text="Options Screen", fg='black', font=Fonts.HEADER.value)
        home_button = tk.Button(self, text="Back", fg='black', width=10,
                                command=lambda: controller.show_frame(StartScreen))

        title_label.pack()
        home_button.pack()


class EndScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self, text="End Screen", fg='black', font=Fonts.HEADER.value)
        retry_button = tk.Button(self, text="Retry?", fg='black', width=10,
                                 command=lambda: controller.show_frame(QuestionScreen1))

        title_label.pack()
        retry_button.pack()
