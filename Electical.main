test_kw_hours = [1500, 764, 1215, 812]
rate_first_1000 = 7.633
rate_above_1000 = 9.259
for i in range(len(test_kw_hours)):
    kw_hours = test_kw_hours[i]
    if kw_hours <= 1000:
        total_cents = kw_hours * rate_first_1000
    else:
        total_cents = (1000 * rate_first_1000) + ((kw_hours - 1000) * rate_above_1000)
        total_dollars = total_cents / 100
        print(f"KW hours used: {kw_hours} → Amount owed is ${total_dollars:.5f}")