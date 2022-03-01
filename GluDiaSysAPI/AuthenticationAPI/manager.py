from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self,email,username,password=None,mobile=None):
        print("Manager")
        if username is None:
            raise TypeError("Username must be set")
        if email is None:
            raise TypeError("Email must be set")

        user=self.model(username=username,email=self.normalize_email(email),mobile=mobile)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,username,password=None,mobile=None):
        if username is None:
            raise TypeError("Username must be set")
        if email is None:
            raise TypeError("Email must be set")
        if password is None:
            raise TypeError("Password must not be none")

       
        user=self.create_user(email,username,password,mobile)
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user