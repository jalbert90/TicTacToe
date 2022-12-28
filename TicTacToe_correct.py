import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe")

status_label = tk.Label(root, text="X turn", font=('Ariel', 16), bg='green', fg='snow')
status_label.pack(fill=tk.X)

current_char = "X"

play_area = tk.Frame(root, width=300, height=300, bg='white')

XPoints = []
OPoints = []
allPoints = []

def resetBtnClick():
    current_char = "X"

    for point in allPoints:
        point.button.configure(state=tk.NORMAL)
        point.reset()

    status_label.configure(text="X turn")
    resetBtn.pack_forget()

resetBtn = tk.Button(root, text="reset", font=('Ariel, 16'), command=resetBtnClick)

class GridCell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
        self.button = tk.Button(play_area, text="", width=10, height=5, command=self.set)
        self.button.grid(row=x, column=y)

    def set(self):
        global current_char

        if not self.value:
            self.button.configure(text=current_char, bg='white', fg='black')
            self.value = current_char

            if current_char == "X":
                status_label.configure(text="O turn")
                XPoints.append(self)
                current_char = "O"
            elif current_char == "O":
                status_label.configure(text="X turn")
                OPoints.append(self)
                current_char = "X"

        check_winner()

    def reset(self):
        if self.value == "X":
            XPoints.remove(self)
        if self.value == "O":
            OPoints.remove(self)

        self.button.configure(text="", bg='white')
        self.value = None

for x in range(1, 4):
    for y in range(1, 4):
        allPoints.append(GridCell(x, y))

class WinningCombo:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def check(self, charToCheck):
        winPos1 = False
        winPos2 = False
        winPos3 = False

        if charToCheck == 'X':
            for xpoint in XPoints:
                if xpoint.x == self.x1 and xpoint.y == self.y1:
                    winPos1 = True
                if xpoint.x == self.x2 and xpoint.y == self.y2:
                    winPos2 = True
                if xpoint.x == self.x3 and xpoint.y == self.y3:
                    winPos3 = True

        if charToCheck == 'O':
            for opoint in OPoints:
                if opoint.x == self.x1 and opoint.y == self.y1:
                    winPos1 = True
                if opoint.x == self.x2 and opoint.y == self.y2:
                    winPos2 = True
                if opoint.x == self.x3 and opoint.y == self.y3:
                    winPos3 = True

        return all([winPos1, winPos2, winPos3])

WinningCombos = [
    WinningCombo(1, 1, 1, 2, 1, 3),
    WinningCombo(2, 1, 2, 2, 2, 3),
    WinningCombo(3, 1, 3, 2, 3, 3),
    WinningCombo(1, 1, 2, 1, 3, 1),
    WinningCombo(1, 2, 2, 2, 3, 2),
    WinningCombo(1, 3, 2, 3, 3, 3),
    WinningCombo(1, 1, 2, 2, 3, 3),
    WinningCombo(1, 3, 2, 2, 3, 1)]

def disable():
    for point in allPoints:
        point.button.configure(state=tk.DISABLED)
        resetBtn.pack()

def check_winner():
    for winCombo in WinningCombos:
        if winCombo.check('X'):
            disable()
            status_label.configure(text="X wins!")
            print("X wins!")
        if winCombo.check('O'):
            disable()
            status_label.configure(text="O wins!")
            print("O wins!")

    if len(XPoints) + len(OPoints) == 9:
        status_label.configure(text="Draw!")
        print("Draw!")
        disable()

play_area.pack(pady=10, padx=10)

root.mainloop()