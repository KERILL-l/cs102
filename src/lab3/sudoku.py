import pathlib
import typing as tp
from math import ceil
from random import randint, shuffle

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Читает Судоку из указанного файла
    :param path: путь до файла
    :return: прочитанный судоку
    """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    """ Создает сетки судоку на основе строк
        :param puzzle: судоку в строковом виде
        :return: сетка судоку
        """
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """
    Отображает Судоку
    :param grid: судоку в виде сетки
    """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировывает значения values в список, состоящий из списков по n элементов
    :param values: изначальный список
    :param n: кол-во элементов будущих подсписков
    :return: список из подсписков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    matrix = [values[i:i + n] for i in range(0, len(values), n)]
    return matrix


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    :param grid: судоку в виде сетки
    :param pos: позиция в сетке искомого элемента
    :return: строка, в которой находится элемент
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row, col = pos
    return grid[row]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    :param grid: судоку в виде сетки
    :param pos: позиция в сетке искомого элемента
    :return: столбец, в котором находится элемент
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    row, col = pos
    return [grid[i][col] for i in range(len(grid))]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    :param grid: судоку в виде сетки
    :param pos: позиция в сетке искомого элемента
    :return: блок, в котором находится элемент
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    row, col = pos
    block_row = ceil((row + 1) / 3)
    if block_row == 1:
        check_row = range(0, 3)
    elif block_row == 2:
        check_row = range(3, 6)
    elif block_row == 3:
        check_row = range(6, 9)
    block_col = ceil((col + 1) / 3)
    if block_col == 1:
        check_col = (0, 3)
    elif block_col == 2:
        check_col = (3, 6)
    elif block_col == 3:
        check_col = (6, 9)
    block = []
    for i in check_row:
        block += grid[i][check_col[0]:check_col[1]]
    return block


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Находит первую свободную позицию в пазле
    :param grid: судоку в виде сетки
    :return: позиция первой пустой позиции
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '.':
                return (i, j)
    return None


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Возвращает множество возможных значений для указанной позиции
    :param grid: судоку в виде сетки
    :param pos: позиция в сетке искомого элемента
    :return: множество возможных значений
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    potential = {str(x) for x in range(1, 10)}
    potential -= {el for el in get_row(grid, pos) if el != '.'}
    potential -= {el for el in get_col(grid, pos) if el != '.'}
    potential -= {el for el in get_block(grid, pos) if el != '.'}
    return potential


def empty_count(grid: tp.List[tp.List[str]]) -> int:
    """
    Возвращает количество пустых ячеек в судоку
    :param grid: судоку в виде сетки
    :return: количество пустых ячеек
    >>> empty_count([['1', '.'], ['.', '2']])
    2
    >>> empty_count([['1', '1'], ['2', '2']])
    0
    """
    count = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] == '.':
                count += 1
    return count


grid_memory = {}


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """
    Решает судоку, заданное в grid :param grid: судоку в виде сетки :return: решенное судоку >>> grid = read_sudoku(
    'puzzle1.txt') >>> solve(grid) [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5',
    '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1',
    '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1',
    '7', '9']]
    """
    if empty_count(grid) == 0:
        return grid

    grid_memory[empty_count(grid)] = [a.copy() for a in grid].copy()
    for potential_solution in find_possible_values(grid, find_empty_positions(grid)):
        pos = find_empty_positions(grid)
        empty_number = empty_count(grid)
        if pos:
            grid[pos[0]][pos[1]] = potential_solution
            check = solve(grid)
            if check:
                return check
            if empty_count(grid) == 0:
                return grid
            grid = [element.copy() for element in grid_memory[empty_number]].copy()


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """
    Проверяет судоку на решенность
    :param solution: судоку в виде сетки
    :return: является ли судоку решенным
    >>> grid = [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    >>> check_solution(grid)
    True
    >>> grid = [['5', '1', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    >>> check_solution(grid)
    False
    """
    if empty_count(solution) != 0:
        return False
    a = [(x, y) for x in range(0, 9, 3) for y in range(0, 9, 3)]
    for i in a:
        if len(set(get_row(solution, i))) == 9 and len(set(get_col(solution, i))) == 9 and len(
                set(get_block(solution, i))) == 9:
            continue
        else:
            return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерирует судоку заполненного на N элементов
    :param N: кол-во элементов в судоку
    :return: судоку из N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    n = 81 - N
    coords = [(x, y) for x in range(0, 9) for y in range(0, 9)]
    shuffle(coords)
    coords = coords[:n]
    grid = solve([['.' for _ in range(9)] for _ in range(9)])
    for x, y in coords:
        grid[x][y] = '.'
    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        # display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
