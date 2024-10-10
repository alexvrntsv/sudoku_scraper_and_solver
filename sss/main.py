from sudoku_scraper import SudokuScraper


def main():
    scraper = SudokuScraper()
    scraper.get_puzzle()
    puzzle = scraper.sudoku_puzzle
    print(puzzle)


if __name__ == "__main__":
    main()
