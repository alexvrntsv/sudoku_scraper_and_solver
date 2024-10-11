from sudoku_scraper import SudokuScraper
from sudoku_gui import SudokuGui
import tkinter as tk


def main():
    scraper = SudokuScraper()
    puzzle = scraper.sudoku_puzzle
    root = tk.Tk()
    gui = SudokuGui(root, scraper)
    root.mainloop()


if __name__ == "__main__":
    main()
