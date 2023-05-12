from secrets import token_urlsafe

# mtd creates a new key when run
def key():
    print(token_urlsafe(12))

# method 'key' is called when the pgm is run
if __name__ == "__main__":
    key()