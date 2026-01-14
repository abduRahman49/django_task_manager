from tasks.models import CustomUser
from core.exceptions import UserAlreadyExists


class AuthenticationService:

    @staticmethod
    def register_user(username, email, password, name=None, surname=None):
        if CustomUser.objects.filter(username=username).exists():
            raise UserAlreadyExists("L'utilisateur avec ce nom d'utilisateur existe déjà")

        user = CustomUser(username=username, email=email, password=password)
        if name is not None:
            user.first_name = name
        
        if surname is not None:
            user.last_name = surname
        
        user.save()
        return user
