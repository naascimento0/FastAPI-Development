from passlib.context import CryptContext

# telling to passlib what is the hashing algorithm
pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_content.hash(password)