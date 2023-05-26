import tkinter as tk
from tkinter import messagebox, scrolledtext

class Hanoi:
    def __init__(self, disks):
        self.disks = disks
        self.total_moves = 0
        self.moves = []

    def solve(self, n=None, source='A', target='C', auxiliary='B'):
        if n is None:
            n = self.disks

        if n > 0:
            self.solve(n - 1, source, auxiliary, target)
            self.moves.append((source, target))
            self.total_moves += 1
            self.solve(n - 1, auxiliary, target, source)

    def print_moves(self, text_widget):
        n = self.disks
        if n > 10:
            text_widget.insert(tk.END, f'Total moves: {self.total_moves}\n')
        else:
            for move in self.moves:
                text_widget.insert(tk.END, f"Move disk  from {move[0]} to {move[1]}\n")


class HanoiGUI:
    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root)
        self.solve_button = tk.Button(root, text='Solve', command=self.solve_hanoi)
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)

        self.entry.pack()
        self.solve_button.pack()
        self.text_area.pack()

    def solve_hanoi(self):
        # Clear the text area
        self.text_area.delete('1.0', tk.END)

        disks = int(self.entry.get())
        hanoi = Hanoi(disks)
        hanoi.solve()
        hanoi.print_moves(self.text_area)
        messagebox.showinfo('Hanoi', f'Total moves: {hanoi.total_moves}')


root = tk.Tk()
gui = HanoiGUI(root)
root.mainloop()
