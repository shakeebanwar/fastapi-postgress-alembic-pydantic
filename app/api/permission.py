from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends,HTTPException,status
from decouple import config
import jwt


def jwtVerify(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    
    try:
        jwt_secret = config("superadminjwttoken")
        jwt_algorithm = "HS256"
        payload = jwt.decode(credentials.credentials, jwt_secret, algorithms=[jwt_algorithm])
        user_id = payload["id"]
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
