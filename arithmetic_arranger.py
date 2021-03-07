import re

def arithmetic_arranger(problems, show_result = False):

    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    # Comprobamos al longitud de la entrada
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # En primer lugar separamos la cadena en {Numero, Signo, Numero}
    for problem in problems:

        list_split = problem.split(' ')
        
        # Comprobar si son dos números
        if not list_split[0].isdecimal() or not list_split[2].isdecimal():
            return 'Error: Numbers must only contain digits.'

        if len(list_split[0]) > 4 or len(list_split[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if not list_split[1] == '+' and not list_split[1] == '-':
            return "Error: Operator must be '+' or '-'."

        if (len(list_split[0]) >= len(list_split[2])):
            len_print = len(list_split[0]) + 2
        else:
            len_print = len(list_split[2]) + 2

        if list_split[1] == '+':
            result = int(list_split[0]) + int(list_split[2])
        elif list_split[1] == '-':
            result = int(list_split[0]) - int(list_split[2])
        else:
            result = 0

        # TODO: Describir correctamente la estrategia de representacion.
        if problem == problems[-1]:
            first_line += '{0:>{len}}'.format(list_split[0], len = len_print)
            second_line += '{0:<} {1:>{len}}'.format(list_split[1], list_split[2], len = len_print - 2)
            third_line += '{:-<{len}}'.format('',len = len_print)
            fourth_line += '{0:>{len}}'.format(result, len = len_print)
        else:
            first_line += '{0:>{len}}    '.format(list_split[0], len = len_print)
            second_line += '{0:<} {1:>{len}}    '.format(list_split[1], list_split[2], len = len_print - 2)
            third_line += '{:-<{len}}    '.format('',len = len_print)
            fourth_line += '{0:>{len}}    '.format(result, len = len_print)

    arranged_problems = first_line + '\n' + second_line + '\n' + third_line

    if show_result:
        arranged_problems += '\n' + fourth_line

    return arranged_problems
