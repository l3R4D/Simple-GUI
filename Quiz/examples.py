import tkinter as tk
import tkinter.messagebox

from Quiz.utils import WindowSettings


# Events for buttons and other triggers
def print_name(event):
    print("Bradley!")


def button_click():
    print("A button has been clicked")


def left_click(event):
    print("Left click")


def right_click(event):
    print("Right click")


# Layout methods
def buttons(root):  # 'root' = tkinter.Tk() window
    """
    Displays four buttons that demonstrates framing and positioning.
    :param root: tkinter.Tk()
    :return: None
    """
    # Make some frames
    top_frame = tk.Frame(root)
    bottom_frame = tk.Frame(root)

    # Make some buttons
    button1 = tk.Button(top_frame, text="Button 1", fg='green')
    button2 = tk.Button(top_frame, text="Button 2", fg='Green')
    button3 = tk.Button(bottom_frame, text="Button 3", fg='blue')
    button4 = tk.Button(bottom_frame, text="Button 4", fg='blue')

    # Pack widgets on 'root'
    top_frame.pack(side=tk.TOP)
    bottom_frame.pack(side=tk.BOTTOM)
    button1.pack(side=tk.LEFT)
    button2.pack(side=tk.LEFT)
    button3.pack(side=tk.RIGHT)
    button4.pack(side=tk.RIGHT)


def labels_one(root):  # 'root' = tkinter.Tk() window
    """
    Displays three labels that demonstrate fill widths and heights.
    :param root: tkinter.Tk()
    :return: None
    """
    # Make some labels
    one = tk.Label(root, text="One", bg='red', fg='white')
    two = tk.Label(root, text="Two", bg='green', fg='black')
    three = tk.Label(root, text="Three", bg='blue', fg='white')

    # Pack widgets on 'root'
    one.pack()
    two.pack(fill=tk.X)
    three.pack(side=tk.LEFT, fill=tk.Y)


def writable_boxes(root):  # 'root' = tkinter.Tk() window
    """
    Displays labels and writable boxes in a grid layout
    :param root: tkinter.Tk()
    :return: None
    """
    # Make some labels 'entries', and check buttons
    label_one = tk.Label(root, text="Name")
    label_two = tk.Label(root, text="Password")
    entry_one = tk.Entry(root)
    entry_two = tk.Entry(root)
    c = tk.Checkbutton(root, text="Keep me logged in")

    # Pack widgets on 'root'
    label_one.grid(row=0, column=0)
    label_two.grid(row=1, column=0)
    entry_one.grid(row=0, column=1)
    entry_two.grid(row=1, column=1)
    c.grid(columnspan=2)


def button_event_one(root):  # 'root' = tkinter.Tk()
    """
    Displays a clickable button that prints a name to the terminal.
    :param root: tkinter.Tk()
    :return: None
    """
    # Make button
    button_one = tk.Button(root, text="Print thine name!")

    # Bind button to an event
    button_one.bind('<Button-1>', print_name)

    # Pack widgets on 'root'
    button_one.pack()


def mouse_button_fun(root):  # 'root' = tkinter.Tk()
    """
    Tracks mouse button clicks and displays clicked buttons in the terminal.
    (Cannot call on a grid)
    :param root: tkinter.Tk()
    :return: None
    """
    # Make tracking frame
    frame = tk.Frame(root, width=WindowSettings.WIDTH.value, height=WindowSettings.HEIGHT.value)

    # Assign methods to button clicks
    frame.bind('<Button-1>', left_click)
    frame.bind('<Button-2>', right_click)

    # Pack widgets on 'root'
    frame.pack()


def tool_bar(root):  # 'root' = tkinter.Tk()
    """
    Basic toolbar.
    :param root: tkinter.Tk()
    :return: None
    """
    # Make toolbar frame
    toolbar = tk.Frame(root, bg='blue')

    # Make some buttons
    insert_button = tk.Button(toolbar, text="Insert Image", command=button_click)
    print_button = tk.Button(toolbar, text="Print", command=button_click)

    # Pack widgets on 'root'
    toolbar.pack(side=tk.TOP, fill=tk.X)
    insert_button.pack(side=tk.LEFT, padx=2, pady=2)
    print_button.pack(side=tk.LEFT, padx=2, pady=2)


def status_bar(root):  # 'root' = tkinter.Tk()
    status = tk.Label(root, text="Preparing...", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status.pack(side=tk.BOTTOM, fill=tk.X)


def pop_up():  # 'root' = tkinter.Tk()
    """
    Basic window popup.
    :return: None
    """
    # Make popup window (Title, description)
    pop_up_one = tkinter.messagebox.askquestion("Brad's Window", "Can you yeet you skeet?")

    # Do something based on the yes or no response response
    if pop_up_one == "yes":
        print("They can skeet their yeet")
    elif pop_up_one == "no":
        print("They cannot skeet their yeet")


class BasicButtons:
    """
    Basic class demonstrating the use of classes within tkinter usage.
    """
    def __init__(self, root):  # 'root' = tkinter.Tk()
        # Make a frame and some buttons
        frame = tk.Frame(root)
        self.print_button = tk.Button(frame, text="Print", command=self.print_message)
        self.quit_button = tk.Button(frame, text="Quit", command=quit)

        # Pack the frame and buttons on 'root'
        frame.pack()
        self.print_button.pack(side=tk.LEFT)
        self.quit_button.pack(side=tk.LEFT)

    # The most simple method to demonstrate tkinter use
    def print_message(self):
        print("Woo!")
