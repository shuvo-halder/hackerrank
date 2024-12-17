import os,sys

def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart


if __name__ == '__main__':
    cart1 = add_to_cart('laptop')
    print(cart1)

    cart2 = add_to_cart('iphone')
    print(cart2)