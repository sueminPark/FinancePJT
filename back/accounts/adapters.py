from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data

        user = super().save_user(request, user, form, False)


        financial_products = data.get("financial_products")
        age = data.get("age")
        money = data.get("money")
        salary = data.get("salary")
        nickname = data.get("nickname")

        
        if financial_products:
            user.financial_products = financial_products
        if age:
            user.age = age
        if money:
            user.money = money
        if salary:
            user.salary = salary
        if nickname:
            user.nickname = nickname

        user.save()
        return user