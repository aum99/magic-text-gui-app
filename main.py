from tkinter import *

MAIN = "#588157"
BOX = "#a3b18a"

timer = 0
is_not_typing = False

class MagicText:

    def __init__(self):

        self.window = Tk()
        self.window.config(padx=40, pady=40, bg=MAIN)
        self.window.title("Magic Text")

        self.typing_box = Text(height=5, bg="#3a5a40", bd=50, fg="#000000", font=("Verdana", 20), highlightthickness=0)
        self.typing_box.focus()
        self.typing_box.grid(row=2, column=0)
        self.typing_box.bind("<Key>", self.check_input)

        self.text_label = Label(self.window, text="MAGIC TEXT APPLICATION", bg=MAIN, bd=50, fg="#000000", font=("Verdana", 20))
        self.text_label.grid(row=1, column=0)

        self.timer_label = Label(self.window, bg=MAIN, bd=50, fg="#000000", font=("Verdana", 20))
        self.timer_label.grid(row=3, column=0)

        self.window.mainloop()

    def countdown(self):
        global is_not_typing

        if is_not_typing:
            global timer
            timer += 1
            self.timer_label.config(text=f"The text will disappear if timer reaches 5 ----> timer: {timer}")
            if timer >= 5:
                self.clear_text()
                is_not_typing = False
                self.typing_box.config(state="disabled")

            self.window.after(1000, self.countdown)

    def reset_timer(self):
        global timer
        timer = 0

    def check_input(self, event=None):
        global is_not_typing
        if is_not_typing:
            self.reset_timer()
        else:
            is_not_typing = True
            self.typing_box.config(highlightbackground="white", highlightcolor="white")
            self.countdown()

    def clear_text(self):
        self.timer_label.config(text=f"Your timer has ended")
        self.typing_box.delete("1.0", END)
        self.reset_timer()

game = MagicText()