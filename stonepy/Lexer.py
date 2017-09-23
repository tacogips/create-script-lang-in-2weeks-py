import re
import string


class Lexer:

    _token_pattern_string = r'"(' + '\\'+ r'|[^"]||\n)*"' # TODO maybe miss escape char

    _token_special_symbols = '|'.join(
        [r'==', r'<=', r'>=', r'&&', '\\', r'|', r'\p{P}'])
    _token_symbols = r'[a-zA-Z_]\w*' + '|' + \
        _token_special_symbols  # not allow start with a number

    _token_regex = re.compile('{0}(({1})|({2})|({3})|{4})?'.format(
        r'\s*',
        r'//.*',
        r'\d',
        _token_pattern_string,
    ))


print(Lexer._TOKEN_SYMBOLS)
