from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from repository import AuthUser

oauth_scheme_home = OAuth2PasswordBearer(tokenUrl='/home')
oauth_scheme_adm = OAuth2PasswordBearer(tokenUrl='/adm')

#Dependecy that verifies the access_token 
def token_verifier_home(token = Depends(oauth_scheme_home)):
    auth_user = AuthUser()
    auth_user.verify_token(token)

#Dependecy that verifies if the access token payload 'sub' is equal to admin
def verify_adm(token = Depends(oauth_scheme_adm)):
    auth_user = AuthUser()
    auth_user.verify_admin(token)