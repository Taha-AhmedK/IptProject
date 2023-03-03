def get_bill(tray):
    # Price calculation
    sub_total = 0
    for eachDish in tray:
        sub_total += eachDish.Price
    tax = round(0.05 * sub_total)
    shipping = 50
    grand_total = sub_total + tax + shipping
    bill = {'sub_total': sub_total, 'tax': tax, 'shipping': shipping, 'grand_total': grand_total}
    return bill