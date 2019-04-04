import tkinter as tk
import random

from utils import Fonts


def questions(container, question, answer1, answer2, answer3, answer4, right_command, wrong_command):
    """
    Reusable method to reduce clutter when making new question screens.
    This method will construct and randomly place four questions on the question frame.
    Each answer button initiates a command, a correct question command and an incorrect question command.
    These two commands must be specified when calling this method. See Question1 for correct usage!
    :param container: tk.Frame()
    :param question: String
    :param answer1: String
    :param answer2: String
    :param answer3: String
    :param answer4: String
    :param right_command: Function
    :param wrong_command: Function
    :return: None
    """
    # Construct our labels and buttons and set their values.
    # 'text' is the text on the button. We are passing a configurable variable into it that will act as a substitute.
    # 'fg' is our foreground. The foreground is the color of the text.
    # 'width' is our set width for the button. By default, all button's widths are set to the width of the text inside.
    # 'pady' is our vertical padding. This gives the text more vertical room within the button.
    question_label = tk.Label(container, text=question, fg='black', font=Fonts.HEADER.value)
    answer_button1 = tk.Button(container, text=answer1, fg='black', width=10, pady=10,
                               command=right_command)
    answer_button2 = tk.Button(container, text=answer2, fg='black', width=10, pady=10,
                               command=wrong_command)
    answer_button3 = tk.Button(container, text=answer3, fg='black', width=10, pady=10,
                               command=wrong_command)
    answer_button4 = tk.Button(container, text=answer4, fg='black', width=10, pady=10,
                               command=wrong_command)

    # Here we throw our buttons in an array for easy picking.
    # We also create an empty array to store our randomly selected numbers. This will help our tool later.
    # Last but not least we select a random number between 0 and the number equal to the length of our buttons array.
    buttons = [answer_button1, answer_button2, answer_button3, answer_button4]
    packed_buttons = []
    selector = random.randint(0, len(buttons) - 1)

    # Order is very important! We must display the question then display our four answers.
    question_label.pack()

    # For every button inside of the buttons array, we are going to display a random answer button on the screen
    # and store the random number in the packed_buttons array. We will then select another random number but we will
    # then check to see if that number has already been used. If so, we will roll for another one until we don't get
    # any numbers from the packed_buttons array.
    for button in buttons:
        while selector in packed_buttons:
            selector = random.randint(0, len(buttons) - 1)
        buttons[selector].pack()
        packed_buttons.append(selector)
        selector = random.randint(0, len(buttons) - 1)


class Quiz(tk.Tk):
    """
    This is the main class that will run when our code starts.
    This class contains all the 'frames' this project will contain and has all the methods necessary for frame
    transition and manipulation.
    """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Here we create a container for all of our elements to reside in. We also give it a padding of 10 pixels
        # around the whole border and allow the container to expand to the size of the window.
        container = tk.Frame(self)
        container.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Here we make an empty dictionary to store all of our frames in.
        # Frames are essentially screens that are formatted differently from one another.
        self.frames = {}
        # For every frame we add here, it will be added to the empty dictionary.
        for F in (StartScreen, QuestionScreen1, OptionScreen, EndScreen):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        # We start the application with this screen.
        self.show_frame(StartScreen)

    # This method will show whatever screen we specify it to show.
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class QuestionScreen1(tk.Frame):
    """
    This is our question screen. Here, we create four buttons and a header thanks to our questions() method.
    Along with the questions, this screen assigns text and commands to the buttons created by the questions() method.
    This class can be copy/pasted if you want to make another question.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Here we call our questions() method. Order here is also super important. Use this as a guide when calling
        # this method.
        questions(self, "What is a bee?", "Insect", "Plant", "Chemical", "Animal",
                  lambda: controller.show_frame(StartScreen), lambda: controller.show_frame(EndScreen))

        # This back button takes us back to the start screen while removing all of the user's progress.
        back_button = tk.Button(self, text="Back", fg='black', width=10,
                                command=lambda: controller.show_frame(StartScreen))
        back_button.pack(side=tk.BOTTOM)


class StartScreen(tk.Frame):
    """
    This is our start screen. Here we create three things: a header, a start button, and an options button.
    """
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
    """
    This is our options screen. It is barren at the moment but it is a blank canvas for you to paint and change,
    so have at it!
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self, text="Options Screen", fg='black', font=Fonts.HEADER.value)
        home_button = tk.Button(self, text="Back", fg='black', width=10,
                                command=lambda: controller.show_frame(StartScreen))

        title_label.pack()
        home_button.pack()


class EndScreen(tk.Frame):
    """
    This is our end screen. Much like the options screen, it is quite empty. Edit it however you wish.
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self, text="End Screen", fg='black', font=Fonts.HEADER.value)
        retry_button = tk.Button(self, text="Retry?", fg='black', width=10,
                                 command=lambda: controller.show_frame(QuestionScreen1))

        title_label.pack()
        retry_button.pack()
