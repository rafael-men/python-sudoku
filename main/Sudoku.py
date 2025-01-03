import pygame as pg
import random 
import math

## cores ##
preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (100,100,255) 
vermelho_dark = (139,0,0)
branco = (255,255,255)



## tela ##
window = pg.display.set_mode((1000,700))
pg.display.set_caption("Sudoku")
pg.font.init()
font_path = "font/Lacquer-Regular.ttf"
font = pg.font.SysFont(font_path,50, bold=True)


table_data =     [['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n']]


game_data =      [['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n'],
                  ['n','n','n','n','n','n','n','n','n']]


## variáveis globais ##

hide_numbers = True
full_table = True 
click_last_status = False
click_position_x = -1
click_position_y = -1
number = 0




## funções ##

def table_hover(window, mouse_position_x, mouse_position_y):
    square = 66.7
    adjust = 50
    x = (math.ceil((mouse_position_x - adjust) /  square ) - 1)
    y = (math.ceil((mouse_position_y - adjust) /  square ) - 1)
    pg.draw.rect(window, preto, (0, 0, 1000, 700))
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, azul, ((adjust + x *  square , adjust + y *  square ,  square ,  square )))

def selected_cell(window, mouse_position_x, mouse_position_y, click_last_status, click, x, y):
    square = 66.7
    adjust = 50
    if click_last_status == True and click == True:
        x = (math.ceil((mouse_position_x - adjust) / square) - 1)
        y = (math.ceil((mouse_position_y - adjust) /square) - 1)
    if x >= 0 and x <= 8 and y >= 0 and y <= 8:
        pg.draw.rect(window, azul, ((adjust + x * square, adjust + y * square, square, square)))
    return x, y

def table(window):
    pg.draw.rect(window,branco, (50, 50, 600, 600), 6)
    pg.draw.rect(window,branco, (50, 250, 600, 200), 6)
    pg.draw.rect(window,branco, (250, 50, 200, 600), 6)
    pg.draw.rect(window,branco, (50, 117, 600, 67), 2)
    pg.draw.rect(window,branco, (50, 317, 600, 67), 2)
    pg.draw.rect(window,branco, (50, 517, 600, 67), 2)
    pg.draw.rect(window,branco, (117, 50, 67, 600), 2)
    pg.draw.rect(window,branco, (317, 50, 67, 600), 2)
    pg.draw.rect(window,branco, (517, 50, 67, 600), 2)

def restart_button(window):
    pg.draw.rect(window, vermelho_dark, (700, 50, 250, 100))
    word = font.render('Restart', True, branco)
    window.blit(word, (725, 75))

def selected_line(table_data, y):
    sorted_line = table_data[y]
    return sorted_line

def selected_column(table_data, x):
    sorted_column = []
    for n in range(8):
        sorted_column.append(table_data[n][x])
    return sorted_column

def selected_quadrant(table_data, x, y):
    quadrant = []
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        quadrant.extend([table_data[0][0], table_data[0][1], table_data[0][2],
                          table_data[1][0], table_data[1][1], table_data[1][2],
                          table_data[2][0], table_data[2][1], table_data[2][2]])
    elif x >= 3 and x <= 5 and y >= 0 and y <= 2:
        quadrant.extend([table_data[0][3], table_data[0][4], table_data[0][5],
                          table_data[1][3], table_data[1][4], table_data[1][5],
                          table_data[2][3], table_data[2][4], table_data[2][5]])
    elif x >= 6 and x <= 8 and y >= 0 and y <= 2:
        quadrant.extend([table_data[0][6], table_data[0][7], table_data[0][8],
                          table_data[1][6], table_data[1][7], table_data[1][8],
                          table_data[2][6], table_data[2][7], table_data[2][8]])
    elif x >= 0 and x <= 2 and y >= 3 and y <= 5:
        quadrant.extend([table_data[3][0], table_data[3][1], table_data[3][2],
                          table_data[4][0], table_data[4][1], table_data[4][2],
                          table_data[5][0], table_data[5][1], table_data[5][2]])
    elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
        quadrant.extend([table_data[3][3], table_data[3][4], table_data[3][5],
                          table_data[4][3], table_data[4][4], table_data[4][5],
                          table_data[5][3], table_data[5][4], table_data[5][5]])
    elif x >= 6 and x <= 8 and y >= 3 and y <= 5:
        quadrant.extend([table_data[3][6], table_data[3][7], table_data[3][8],
                          table_data[4][6], table_data[4][7], table_data[4][8],
                          table_data[5][6], table_data[5][7], table_data[5][8]])
    elif x >= 0 and x <= 2 and y >= 6 and y <= 8:
        quadrant.extend([table_data[6][0], table_data[6][1], table_data[6][2],
                          table_data[7][0], table_data[7][1], table_data[7][2],
                          table_data[8][0], table_data[8][1], table_data[8][2]])
    elif x >= 3 and x <= 5 and y >= 6 and y <= 8:
        quadrant.extend([table_data[6][3], table_data[6][4], table_data[6][5],
                          table_data[7][3], table_data[7][4], table_data[7][5],
                          table_data[8][3], table_data[8][4], table_data[8][5]])
    elif x >= 6 and x <= 8 and y >= 6 and y <= 8:
        quadrant.extend([table_data[6][6], table_data[6][7], table_data[6][8],
                          table_data[7][6], table_data[7][7], table_data[7][8],
                          table_data[8][6], table_data[8][7], table_data[8][8]])
    return quadrant

def fill_quadrant(table_data, x2, y2):
    filled_quadrant = True
    loop = 0
    try_count = 0
    number = 1
    while filled_quadrant == True:
        x = random.randint(x2, x2 + 2)
        y = random.randint(y2, y2 + 2)
        sorted_line = selected_line(table_data, y)
        sorted_column = selected_column(table_data, x)
        quadrant = selected_quadrant(table_data, x, y)
        if table_data[y][x] == 'n' and number not in sorted_line and number not in sorted_column and number not in quadrant:
            table_data[y][x] = number
            number += 1
        loop += 1
        if loop == 50:
            table_data[y2][x2] = 'n'
            table_data[y2][x2 + 1] = 'n'
            table_data[y2][x2 + 2] = 'n'
            table_data[y2 + 1][x2] = 'n'
            table_data[y2 + 1][x2 + 1] = 'n'
            table_data[y2 + 1][x2 + 2] = 'n'
            table_data[y2 + 2][x2] = 'n'
            table_data[y2 + 2][x2 + 1] = 'n'
            table_data[y2 + 2][x2 + 2] = 'n'
            loop = 0
            number = 1
            try_count += 1
        if try_count == 10:
            break
        count = 0
        for n in range(9):
            if quadrant[n] != 'n':
                count += 1
        if count == 9:
            filled_quadrant = False
    return table_data

def restarting_table_data(table_data):
    table_data = [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
                      ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']]
    return table_data

def table_answer(table_data, full_table):
    while full_table == True:
        table_data = fill_quadrant(table_data, 0, 0)
        table_data = fill_quadrant(table_data, 3, 0)
        table_data = fill_quadrant(table_data, 6, 0)
        table_data = fill_quadrant(table_data, 0, 3)
        table_data = fill_quadrant(table_data, 0, 6)
        table_data = fill_quadrant(table_data, 3, 3)
        table_data = fill_quadrant(table_data, 3, 6)
        table_data = fill_quadrant(table_data, 6, 3)
        table_data = fill_quadrant(table_data, 6, 6)
        for nn in range(9):
            for n in range(9):
                if table_data[nn][n] == 'n':
                    table_data = restarting_table_data(table_data)
        count = 0
        for nn in range(9):
            for n in range(9):
                if table_data[nn][n] != 'n':
                    count += 1
        if count == 81:
            full_table = False
    return table_data, full_table

def hiding_numbers(table_data, game_data, hide_numbers):
    if hide_numbers == True:
        for n in range(9):
            for m in range(9):
                game_data[n][m] = table_data[n][m]
                if random.randint(0, 1) == 0:  
                    game_data[n][m] = 'n'
        hide_numbers = False
    return game_data, hide_numbers

def writing_numbers(window, game_data):
    square = 66.7
    adjust = 67
    for nn in range(9):
        for n in range(9):
            if game_data[nn][n] != 'n':
                word = font.render(str(game_data[nn][n]), True, branco)
                window.blit(word, (adjust + n * square, adjust - 5 + nn * square))
                if game_data[nn][n] == 'X':
                    word = font.render(str(game_data[nn][n]), True, vermelho)
                    window.blit(word, (adjust + n * square, adjust - 5 + nn * square))

def digit_number(number):
    try:
        number = int(number[1])
    except:
        number = int(number)
    return number

def check_digits(window, table_data, game_data, click_position_x, click_position_y, number):
    x = click_position_x
    y = click_position_y
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and table_data[y][x] == number and game_data[y][x] == 'n' and number != 0:
        game_data[y][x] = number
        number = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and table_data[y][x] == number and game_data[y][x] == number and number != 0:
        pass
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and table_data[y][x] != number and game_data[y][x] == 'n' and number != 0:
        game_data[y][x] = 'X'
        number = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and table_data[y][x] == number and game_data[y][x] == 'X' and number != 0:
        game_data[y][x] = number
        number = 0
    return game_data, number

def click_restart(mouse_position_x, mouse_position_y, click_last_status, click, full_table, hide_numbers, table_data, game_data):
    x = mouse_position_x
    y = mouse_position_y
    if x >= 700 and x <= 950 and y >= 50 and y <= 150 and click_last_status == False and click == True:
        full_table = True
        hide_numbers = True
        table_data = restarting_table_data(table_data)
        game_data = restarting_table_data(game_data)
    return full_table, hide_numbers, table_data, game_data

def is_valid_move(board, row, col, number):
    if number in board[row]:
        return False
    for i in range(9):
        if board[i][col] == number:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == number:
                return False
    return True

def validate_input(x, y, number, table_data):
    # Verifica linha, coluna e quadrante para validar o número
    if number in selected_line(table_data, y):
        return False
    if number in selected_column(table_data, x):
        return False
    if number in selected_quadrant(table_data, x, y):
        return False
    return True

def handle_input(event, table_data, x, y):
    if event.key == pg.K_1 or event.key == pg.K_2 or event.key == pg.K_3 or event.key == pg.K_4 or event.key == pg.K_5 or event.key == pg.K_6 or event.key == pg.K_7 or event.key == pg.K_8 or event.key == pg.K_9:
        number = int(event.unicode)
        # Permitir edição da célula selecionada, mesmo que válida
        table_data[y][x] = number
    return table_data


selected_celule = None  

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        
        # Processamento de clique do mouse
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            if 50 <= x <= 650 and 50 <= y <= 650:  
                col = (x - 50) // 66
                row = (y - 50) // 66
                selected_celule = (row, col)

        # Processamento de teclado para preencher a célula
        if event.type == pg.KEYDOWN:
            if selected_celule:
                row, col = selected_celule
                if event.unicode.isdigit(): 
                    number = int(event.unicode)
                    # Permitir edição da célula selecionada
                    game_data[row][col] = number  # Atualiza diretamente, mesmo se válido

    # Atualização da tela
    window.fill(preto)
    table(window)
    
    # Desenha os números na tabela
    for i in range(9):
        for j in range(9):
            if game_data[i][j] != 'n':
                number_surface = font.render(str(game_data[i][j]), True, branco)
                window.blit(number_surface, (50 + j * 66 + 20, 50 + i * 66 + 10))
    
    # Destacar célula selecionada
    if selected_celule:
        row, col = selected_celule
        highlight_rect = pg.Rect(50 + col * 66, 50 + row * 66, 66, 66)
        pg.draw.rect(window, (255, 0, 0), highlight_rect, 3)  

    ## Variáveis de posição do mouse ##
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]
    click = pg.mouse.get_pressed()

    ## Jogo ##
    table_hover(window, mouse_position_x, mouse_position_y)
    click_position_x, click_position_y = selected_cell(window, mouse_position_x, mouse_position_y, click_last_status, click[0], click_position_x, click_position_y)
    table(window)
    restart_button(window)
    table_data, full_table = table_answer(table_data, full_table)
    game_data, hide_numbers = hiding_numbers(table_data, game_data, hide_numbers)
    writing_numbers(window, game_data)
    number = (number)
    game_data, number = check_digits(window, table_data, game_data, click_position_x, click_position_y, number)
    full_table, hide_numbers, table_data, game_data = click_restart(mouse_position_x, mouse_position_y, click_last_status, click[0], full_table, hide_numbers, table_data, game_data)

    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False

    pg.display.update()
