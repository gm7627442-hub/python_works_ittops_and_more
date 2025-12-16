def print_bar(length: int, filled: int) -> None:

    if length < 0:
        length = 0
    if filled < 0:
        filled = 0
    if filled > length:
        filled = length
    
    progress = "#" * filled
    empty = "." * (length - filled)
    
    print(f"[{progress}{empty}]")