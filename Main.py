import tkinter as tk

from Examples import buttons, labels_one, writable_boxes, button_event_one, mouse_button_fun, BasicButtons, tool_bar, \
    status_bar, pop_up


# Initialize
root = tk.Tk()
root.geometry('500x500')


def main():
    # Desired layout and methods
    tool_bar(root)
    status_bar(root)
    buttons(root)
    button_event_one(root)
    labels_one(root)
    mouse_button_fun(root)

    # Display layout and execute methods
    root.mainloop()


if __name__ == '__main__':
    main()
