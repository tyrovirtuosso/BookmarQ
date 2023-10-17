from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user.email = data['email']
        self.populate_username(request, user)
        if commit:
            user.save()
        return user