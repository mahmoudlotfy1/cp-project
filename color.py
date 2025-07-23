


def color_(color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
        }
    def decorator(func):
        def wrapper(*arges,**kwargs):
            result= func(*arges,**kwargs)
            return f"{colors.get(color, colors['reset'])}{result}{colors['reset']}"
        return wrapper
    return decorator
