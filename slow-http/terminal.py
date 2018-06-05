###### Author           Skipper.D
###### DESCRIPTION      Terminal controller
###### VERSION          v1.0
###### UPDATE           2016/01/21


class Terminal:

    UP          = '\x1b[A'  # move cursor up
    DOWN        = '\x1b[B'  # move cursor down
    RIGHT       = '\x1b[C'  # move cursor right
    LEFT        = '\x1b[D'  # move cursor left
    
    ERASE_BOL   = '\x1b[1K' # erase to beginning of line
    ERASE_EOL   = '\x1b[0K' # erase to end of line
    
    RED         = '\x1b[31;1m'
    GREEN       = '\x1b[32;1m'
    YELLOW      = '\x1b[33;1m'
    BLUE        = '\x1b[34;1m'
    MAGENTA     = '\x1b[35;1m'
    CYAN        = '\x1b[36;1m'
    UNDERLINE   = '\x1b[4m'
    NORM        = '\x1b[0m'

