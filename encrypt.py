# encrypt.py
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Custom encryption function (Caesar Cipher)
def encrypt_data(data: str, shift: int) -> str:
    try:
        encrypted = ""
        for char in data:
            if char.isalpha():  # Encrypt only alphabetic characters
                shift_amount = 65 if char.isupper() else 97
                encrypted += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            else:
                encrypted += char  # Leave non-alphabetic characters unchanged
        return encrypted
    except Exception as e:
        raise HTTPException(status_code=500, detail="Encryption failed.")

# Endpoint to encrypt data with a custom shift
@app.post("/encrypt.py")
async def encrypt(data: str, shift: int = 3):
    """
    Encrypt the data with a Caesar Cipher using a custom shift.
    :param data: The text to encrypt.
    :param shift: The number of positions to shift the characters.
    :return: The encrypted text.
    """
    try:
        encrypted_data = encrypt_data(data, shift)
        return {"encrypted_data": encrypted_data}
    except HTTPException as e:
        raise e
