from fastapi import FastAPI, HTTPException

app = FastAPI()

# Custom simple encryption method using character mapping
ENCRYPTION_MAP = {
    "a": "@", "b": "8", "c": "(", "d": "#", "e": "3", "f": "!", "g": "6", "h": "4", "i": "1",
    "j": "?", "k": "<", "l": "7", "m": "M", "n": "N", "o": "0", "p": "%", "q": "Q", "r": "2",
    "s": "$", "t": "+", "u": "U", "v": "V", "w": "W", "x": "*", "y": "Y", "z": "Z"
}

# Reverse mapping for decryption
DECRYPTION_MAP = {v: k for k, v in ENCRYPTION_MAP.items()}

def encrypt_text(plain_text: str) -> str:
    return "".join(ENCRYPTION_MAP.get(char, char) for char in plain_text.lower())

def decrypt_text(encrypted_text: str) -> str:
    return "".join(DECRYPTION_MAP.get(char, char) for char in encrypted_text)

@app.post("/encrypt")
def encrypt(data: dict):
    text = data.get("text")
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    
    encrypted_text = encrypt_text(text)
    return {"encrypted": encrypted_text}

@app.post("/decrypt")
def decrypt(data: dict):
    text = data.get("text")
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")
    
    decrypted_text = decrypt_text(text)
    return {"decrypted": decrypted_text}
