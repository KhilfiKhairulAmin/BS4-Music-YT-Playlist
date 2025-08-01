class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def yellow(t: str) -> str:
        return Colors.YELLOW + t + Colors.RESET
    
    @staticmethod
    def green(t: str) -> str:
        return Colors.GREEN + t + Colors.RESET