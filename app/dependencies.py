from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate(token: str = Depends(oauth2_scheme)):
    if token != "my_secure_token":
        raise HTTPException(status_code=401, detail="Unauthorized")