
def split_parameters(line):
    params = []
    current_param = []
    brackets = {'round': 0, 'square': 0, 'curly': 0}
    in_double_quotes = False
    in_single_quotes = False
    escape = False
    for idx, char in enumerate(line):
        char: str
        char = char.strip()
        if escape:
            current_param.append(char)
            escape = False
        elif char == '\\':
            escape = True
            current_param.append(char)
        else:
            if char == '(':
                brackets['round'] += 1
            elif char == ')':
                brackets['round'] -= 1
            elif char == '[':
                brackets['square'] += 1
            elif char == ']':
                brackets['square'] -= 1
            elif char == '{':
                brackets['curly'] += 1
            elif char == '}':
                brackets['curly'] -= 1
            if char == '"' and not in_single_quotes:
                in_double_quotes = not in_double_quotes
            elif char == "'" and not in_double_quotes:
                in_single_quotes = not in_single_quotes
            current_param.append(char)
        is_comma = char == ','
        end_of_line = idx == len(line) - 1
        can_split = not in_double_quotes and not in_single_quotes and all(count == 0 for count in brackets.values())
        if (is_comma or end_of_line) and can_split:
            if is_comma:
                if current_param:
                    current_param.pop()
            param = ''.join(current_param)
            if param or (is_comma and not end_of_line) or end_of_line:
                params.append(param)
            current_param = []
            brackets = {'round': 0, 'square': 0, 'curly': 0}
            in_double_quotes = False
            in_single_quotes = False
            escape = False
    if current_param:
        params.append(''.join(current_param))
    return params


# def split_parameters(line):
#     params = []
#     param = ''
#     flag_round_bracket = 0
#     flag_square_bracket = 0
#     flag_curly_bracket = 0
#     flag_double_quotes = False
#     flag_single_quotes = False
#     flag_double_quotes_continue = False
#     flag_single_quotes_continue = False
#     length = len(line)
#     for idx, char in enumerate(line):
#         if char == '(':
#             flag_round_bracket += 1
#         elif char == ')':
#             flag_round_bracket -= 1
#         if char == '[':
#             flag_square_bracket += 1
#         elif char == ']':
#             flag_square_bracket -= 1
#         if char == '{':
#             flag_curly_bracket += 1
#         elif char == '}':
#             flag_curly_bracket -= 1
#         if char == '"':
#             if not flag_double_quotes_continue:
#                 if flag_double_quotes:
#                     flag_double_quotes = False
#                 else:
#                     flag_double_quotes = True
#         else:
#             flag_double_quotes_continue = False
#         if char == "'":
#             if not flag_single_quotes_continue:
#                 if flag_single_quotes:
#                     flag_single_quotes = False
#                 else:
#                     flag_single_quotes = True
#         else:
#             flag_single_quotes_continue = False
#         if (
#             (
#                 char == ','
#                 and not flag_round_bracket
#                 and not flag_square_bracket
#                 and not flag_curly_bracket
#                 and not flag_double_quotes
#                 and not flag_single_quotes
#             )
#                 or idx == length - 1):
#             if param:
#                 params.append(param)
#             param = ''
#             flag_round_bracket = 0
#             flag_square_bracket = 0
#             flag_curly_bracket = 0
#             flag_double_quotes = False
#             flag_single_quotes = False
#             flag_double_quotes_continue = False
#             flag_single_quotes_continue = False
#         else:
#             param += char
#     return params
