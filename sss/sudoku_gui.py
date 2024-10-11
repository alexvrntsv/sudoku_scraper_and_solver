import tkinter as tk


class SudokuGui:
    def __init__(self, root, scraper):
        self.root = root
        self.root.title("Sudoku")
        self.scraper = scraper
        scraper.get_puzzle()
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                if self.scraper.sudoku_puzzle[i][j] != 0:
                    cell = tk.Label(self.root, width=2, font=('Arial', 18), justify='center',
                                    text=self.scraper.sudoku_puzzle[i][j])
                else:
                    cell = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center')
                cell.grid(row=i, column=j, padx=1, pady=1)
                self.cells[i][j] = cell

    def create_buttons(self):
        reload_button = tk.Button(self.root, text="Reload Puzzle", command=self.reload_puzzle)
        reload_button.grid(row=10, column=0, columnspan=3)

        check_button = tk.Button(self.root, text="Сheck me", command=self.check_puzzle)
        check_button.grid(row=10, column=3, columnspan=3)

        clear_button = tk.Button(self.root, text="Clear", command=self.clear_puzzle)
        clear_button.grid(row=10, column=6, columnspan=3)

    def reload_puzzle(self):
        self.scraper.get_puzzle()
        self.create_grid()
    def check_puzzle(self):
        print("Check me")

    def clear_puzzle(self):
        print("Clear")


