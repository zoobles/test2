from django import forms
from battleships import utils
from battleships.models import GameUsers
from django.contrib.auth.models import User


class placementForm(forms.Form):
    Aircraft_Carrier_X = forms.CharField(max_length=2, required=False)
    Aircraft_Carrier_Y = forms.CharField(max_length=2, required=False)

    Battleship_X = forms.CharField(max_length=2, required=False)
    Battleship_Y = forms.CharField(max_length=2, required=False)

    Cruiser_X = forms.CharField(max_length=2, required=False)
    Cruiser_Y = forms.CharField(max_length=2, required=False)

    Destroyer_X = forms.CharField(max_length=2, required=False)
    Destroyer_Y = forms.CharField(max_length=2, required=False)

    Submarine_X = forms.CharField(max_length=2, required=False)
    Submarine_Y = forms.CharField(max_length=2, required=False)

    def clean(self):
        data = self.cleaned_data
        acX = data.get('Aircraft_Carrier_X')
        acY = data.get('Aircraft_Carrier_Y')

        baX = data.get('Battleship_X')
        baY = data.get('Battleship_Y')

        crX = data.get('Cruiser_X')
        crY = data.get('Cruiser_Y')

        deX = data.get('Destroyer_X')
        deY = data.get('Destroyer_Y')

        suX = data.get('Submarine_X')
        suY = data.get('Submarine_Y')

        if not acX:
            self.add_error("Aircraft_Carrier_X", "Must give coordinates.")
        if not acY:
            self.add_error("Aircraft_Carrier_Y", "Must give coordinates.")

        if not baX:
            self.add_error("Battleship_X", "Must give coordinates.")
        if not baY:
            self.add_error("Battleship_Y", "Must give coordinates.")

        if not crX:
            self.add_error("Cruiser_X", "Must give coordinates.")
        if not crY:
            self.add_error("Cruiser_Y", "Must give coordinates.")

        if not deX:
            self.add_error("Destroyer_X", "Must give coordinates.")
        if not deY:
            self.add_error("Destroyer_Y", "Must give coordinates.")

        if not suX:
            self.add_error("Submarine_X", "Must give coordinates.")
        if not suY:
            self.add_error("Submarine_Y", "Must give coordinates.")

        if acX and acY:
            acX_start = acX[0]
            acX_end = acX[1:]

            acY_start = acY[0]  # Letter
            acY_end = acY[1:]  # digit

            if acX_start.isdigit():  # if its not a letter
                self.add_error("Aircraft_Carrier_X", "Aircraft-Carrier X coordinate needs to start with a letter ")

            if not acX_end.isdigit():
                self.add_error("Aircraft_Carrier_X", "Aircraft-Carrier X coordinate needs to end in a number")

            if acY_start.isdigit():  # if its not a letter
                self.add_error("Aircraft_Carrier_Y", "Aircraft-Carrier Y coordinate needs to start with a letter ")

            if not acY_end.isdigit():
                self.add_error("Aircraft_Carrier_Y", "Aircraft-Carrier Y coordinate needs to end in a number")

        if baX and baY:
            baX_start = baX[0]
            baX_end = baX[1:]

            baY_start = baY[0]  # Letter
            baY_end = baY[1:]  # digit

            if baX_start.isdigit():  # if its not a letter
                self.add_error("Battleship_X", "Battleship X coordinate needs to start with a letter ")

            if not baX_end.isdigit():
                self.add_error("Battleship_X", "Battleship X coordinate needs to end in a number")

            if baY_start.isdigit():  # if its not a letter
                self.add_error("Battleship_Y", "Battleship Y coordinate needs to start with a letter ")

            if not baY_end.isdigit():
                self.add_error("Battleship_Y", "Battleship Y coordinate needs to end in a number")

        if crX and crY:
            crX_start = crX[0]
            crX_end = crX[1:]

            crY_start = crY[0]  # Letter
            crY_end = crY[1:]  # digit

            if crX_start.isdigit():  # if its not a letter
                self.add_error("Cruiser_X", "Cruiser X coordinate needs to start with a letter ")

            if not crX_end.isdigit():
                self.add_error("Cruiser_X", "Cruiser X coordinate needs to end in a number")

            if crY_start.isdigit():  # if its not a letter
                self.add_error("Cruiser_Y", "Cruiser Y coordinate needs to start with a letter ")

            if not crY_end.isdigit():
                self.add_error("Cruiser_Y", "Cruiser Y coordinate needs to end in a number")

        if deX and deY:
            deX_start = deX[0]
            deX_end = deX[1:]

            deY_start = deY[0]  # Letter
            deY_end = deY[1:]  # digit

            if deX_start.isdigit():  # if its not a letter
                self.add_error("Destroyer_X", "Destroyer X coordinate needs to start with a letter ")

            if not deX_end.isdigit():
                self.add_error("Destroyer_X", "Destroyer X coordinate needs to end in a number")

            if deY_start.isdigit():  # if its not a letter
                self.add_error("Destroyer_Y", "Destroyer Y coordinate needs to start with a letter ")

            if not deY_end.isdigit():
                self.add_error("Destroyer_Y", "Destroyer Y coordinate needs to end in a number")

        if suX and suY:
            suX_start = suX[0]
            suX_end = suX[1:]

            suY_start = suY[0]  # Letter
            suY_end = suY[1:]  # digit

            if suX_start.isdigit():  # if its not a letter
                self.add_error("Submarine_X", "Submarine X coordinate needs to start with a letter ")

            if not suX_end.isdigit():
                self.add_error("Submarine_X", "Submarine X coordinate needs to end in a number")

            if suY_start.isdigit():  # if its not a letter
                self.add_error("Submarine_Y", "Submarine Y coordinate needs to start with a letter ")

            if not suY_end.isdigit():
                self.add_error("Submarine_Y", "Submarine Y coordinate needs to end in a number")


class inviteForm(forms.Form):
    name = forms.CharField(max_length=20, required=True)


class registerForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    username = forms.CharField(max_length=20, required=True)
    password1 = forms.CharField(max_length=100, required=True)
    password2 = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)

    def clean(self):
        data = self.cleaned_data

        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        def validateEmail(email):
            from django.core.validators import validate_email
            from django.core.exceptions import ValidationError
            try:
                validate_email(email)
                return True
            except ValidationError:
                return False

        match = validateEmail(email)
        if not match:
            self.add_error("email", "Email address is not valid")

        if password1 != password2:
            self.add_error("password1", "passwords do not match!")


class loginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        data = self.cleaned_data
        username = data.get('username')

        if not GameUsers.objects.filter(username=username):  # if user isn't in gameusers list
            print "isnt game user"
            self.add_error("username", "this user is not registered as a game user!")


class shootForm(forms.Form):
    coord = forms.CharField(max_length=2, required=True)

    def clean(self):
        data = self.cleaned_data









