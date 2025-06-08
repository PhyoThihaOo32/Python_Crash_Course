def generate_grade_report(name, scores):
    average = sum(scores)/ len(scores)
    status = 'Pass' if average >= 60 else 'Fail'

    return {
        'name': name,
        'average': average,
        'status': status
    }

print(generate_grade_report('Natalia',[90,90,90]))


# e_commerce order summary

def order_summary(item, price, quantity):
    total = price * quantity
    return {
        'item': item,
        'price': price,
        'quantity': quantity,
        'total': total
    }

print(order_summary('Milk',9.99,2))