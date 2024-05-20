import random

def order_pizza(*toppings, **kwargs):
    if len(toppings) < 2:
        print(f"You have to choose at least 2 toppings to proceed")
        return
    if len(toppings) > 7:
        print(f"You have chosen too many toppings!")
        return

    size = kwargs.get('size', 'large')
    crust = kwargs.get('crust', 'thin')

    size_price = {'small': 10, 'medium': 15, 'large': 20}
    crust_price = {'thin': 0, 'thick': 3}
    topping_price = 2
    additional_cost = (len(toppings) - 2) * topping_price

    price = size_price[size] + crust_price[crust] + additional_cost
    order_id = random.randint(10, 99)

    print(f"Order number: {order_id}")
    print(f"Size: {size}")
    print(f"Crust: {crust}")
    print(f"Toppings: {toppings}")
    print(f"Price: ${price}")
    print()

order_pizza('pepperoni', 'extra cheese', 'chorizo', size='large', crust='thick')
order_pizza('buffalo', 'chili', 'sausage', 'mushrooms', 'rucola', size='medium', crust='thin')
order_pizza('pepperoni', 'salami', 'virgin oil', 'pineapple', size='small', crust='thick')

