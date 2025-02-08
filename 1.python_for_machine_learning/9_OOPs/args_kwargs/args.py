# Logging System

def log_message(level, *args):
    print(f"{level}:", end=" ")
    for arg in args:
        print(arg, end=" ")
    print()

log_message("INFO", "Server started successfully")
log_message("ERROR", "Connection failed", "Timeout", "Database")
