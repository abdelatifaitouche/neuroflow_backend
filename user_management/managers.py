from django.contrib.auth.models import BaseUserManager , AbstractUser , UserManager





class CustomUserManager(BaseUserManager):
    

    def create_user(self, email ,username , first_name , last_name , password=None, **extra_fields):
        
        if not email : 
            raise ValueError("Please, enter an email")
        

        email = super().normalize_email(email)

        user = self.model(email = email , username = username , first_name = first_name , last_name = last_name)
        user.set_password(password)
        user.save(using = self.db)

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)
    

    def create_superuser(self, email, username, first_name, last_name, password=None):
        """
        Create and return a superuser with an email, username, and password.
        """
        user = self.create_user(email, username, first_name, last_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user