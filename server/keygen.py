from secrets import token_urlsafe

def key():
    print(token_urlsafe(12))
    
if __name__ == "__main__":
    key()