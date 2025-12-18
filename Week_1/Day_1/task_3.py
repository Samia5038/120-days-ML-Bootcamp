from decimal import Decimal, getcontext
getcontext().prec=5
bill=Decimal("100") / Decimal("3")
print(f"${bill}")