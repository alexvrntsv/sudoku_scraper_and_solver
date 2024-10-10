import requests
from bs4 import BeautifulSoup


class SudokuScraper:
    BASE_URL = "https://west.websudoku.com/?level=1"

    def __init__(self):
        self.sudoku_puzzle = None

    def get_puzzle(self):
        response = requests.get(self.BASE_URL)
        if response.status_code == 200:
            self.sudoku_puzzle = self._parse_puzzle(response.text)
        else:
            raise Exception("Loading Error")

    def _parse_puzzle(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        puzzle = []

        for i in range(9):
            row = []
            for j in range(9):
                cell_id = f"f{i}{j}"
                cell = soup.find("input", {"id": cell_id})

                if cell and cell.has_attr("value"):
                    cell_value = cell["value"]
                    row.append(int(cell_value) if cell_value.isdigit() else 0)
                else:
                    row.append(0)
            puzzle.append(row)

        return puzzle
