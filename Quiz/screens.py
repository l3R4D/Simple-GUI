import tkinter as tk


class QuestionScreen:
    """
    Basic parent class for all Question Screen objects.
    This class contains all the basic, bare bones attributes a question screen needs.
    """
    # These are the variables we fill in when we call this class
    def __init__(self, root, question, answer_1, answer_2, answer_3, real_answer):
        self.question = question
        self.answer_1 = answer_1
        self.answer_2 = answer_2
        self.answer_3 = answer_3
        self.real_answer = real_answer

        # Make our game frames. These will be our invisible boxes that hold our elements
        game_frame = tk.Frame(root)
        question_frame = tk.Frame(game_frame)
        answers_frame = tk.Frame(game_frame)
        toolbar_frame = tk.Frame(game_frame)
        navbar_frame = tk.Frame(game_frame)

        # Make our screen elements. These elements will be inside their respective boxes to further organize.
        question_label = tk.Label(question_frame, text=question, fg='black')
        answer_button_1 = tk.Button(answers_frame, text=answer_1, fg='black', width=10)
        answer_button_2 = tk.Button(answers_frame, text=answer_2, fg='black', width=10)
        answer_button_3 = tk.Button(answers_frame, text=answer_3, fg='black', width=10)
        answer_button_4 = tk.Button(answers_frame, text=real_answer, fg='black', width=10)
        pause_button = tk.Button(toolbar_frame, text="Pause", fg='black')
        options_button = tk.Button(toolbar_frame, text="Options", fg='black')
        next_question_button = tk.Button(navbar_frame, text="====>", fg='black')
        last_question_button = tk.Button(navbar_frame, text="<====", fg='black')

        # Pack all of our elements together onto the screen. Oder is very important here!!!
        game_frame.pack(fill=tk.BOTH, expand=True)
        toolbar_frame.pack(side=tk.TOP, fill=tk.X)
        question_frame.pack(side=tk.TOP, fill=tk.Y)
        answers_frame.pack()
        navbar_frame.pack(side=tk.BOTTOM, fill=tk.X)
        question_label.pack()
        pause_button.pack(side=tk.LEFT)
        options_button.pack(side=tk.LEFT)
        next_question_button.pack(side=tk.RIGHT)
        last_question_button.pack(side=tk.LEFT)
        answer_button_1.pack(side=tk.LEFT)
        answer_button_2.pack(side=tk.LEFT)
        answer_button_3.pack(side=tk.LEFT)
        answer_button_4.pack(side=tk.LEFT)


class StartScreen:
    """
    Base parent class for all Start Screen objects.
    This class contains all the bare bone features a start screen would need.
    """
    def __init__(self, root):
        # Make our frames, or in other words, our invisible boxes
        game_frame = tk.Frame(root)
        title_frame = tk.Frame(game_frame)
        button_frame = tk.Frame(game_frame)

        # Make our elements that will be packed inside of their little boxes
        title_label = tk.Label(title_frame, text="QUIZ", fg='black', font=('', 60))
        options_button = tk.Button(button_frame, text="Options", fg='black', width=10)
        start_button = tk.Button(button_frame, text="Start!", fg='black', width=10)

        # Pack everything onto the screen. Again, order is super important when it comes to packing!
        game_frame.pack(fill=tk.BOTH, expand=True)
        title_frame.pack()
        button_frame.pack()
        title_label.pack()
        start_button.pack()
        options_button.pack()
