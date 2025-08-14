from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def results(request):
    return render(request, 'results.html')

# Amortization calculation function
def generate_amortization_table(principal, annual_interest_rate, years):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    total_payments = years * 12

    monthly_payment = (
        principal *
        (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) /
        ((1 + monthly_interest_rate) ** total_payments - 1)
    )

    balance = principal
    table = []

    for month in range(1, total_payments + 1):
        interest_payment = balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment
        if balance < 0:
            balance = 0

        table.append({
            "month": month,
            "payment": round(monthly_payment, 2),
            "principal": round(principal_payment, 2),
            "interest": round(interest_payment, 2),
            "balance": round(balance, 2)
        })

    return table, monthly_payment


def index(request):
    return render(request, "index.html")


def loan_calculator(request):
    if request.method == "POST":
        try:
            principal = float(request.POST.get("principal"))
            annual_interest_rate = float(request.POST.get("interest_rate"))
            years = int(request.POST.get("years"))

            schedule, monthly_payment = generate_amortization_table(principal, annual_interest_rate, years)

            total_payment = round(monthly_payment * years * 12, 2)
            total_interest = round(total_payment - principal, 2)

            context = {
                "schedule": schedule,
                "monthly_payment": round(monthly_payment, 2),
                "total_payment": total_payment,
                "total_interest": total_interest
            }
            return render(request, "results.html", context)

        except (ValueError, ZeroDivisionError):
            return render(request, "index.html", {"error": "Please enter valid inputs."})

    return render(request, "index.html")
