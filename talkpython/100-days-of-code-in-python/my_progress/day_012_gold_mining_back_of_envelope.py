#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Back of envelope calculations for a precious metals mining company

oz_per_yr = int(input("How many ounces will be produced annually?: "))
price_per_oz = int(input("What is the estimated USD price per ounce for the year?: "))
aisc = int(input("What is the USD AISC?: "))
exchange_rate = float(input("What is the USD/CAD exchange rate?: "))
shrs_out = int(input("How many shares are outstanding?: "))
pe = int(input("What is the estimated PE ratio?: "))


values = {
    'oz_per_yr':     oz_per_yr,
    'price_per_oz':  price_per_oz,
    'aisc':          aisc,
    'exchange_rate': exchange_rate,
    'shrs_out':      shrs_out,
    'pe':            pe
}


def share_price_calc(vals):

    oz_per_yr     = vals['oz_per_yr']
    price_per_oz  = vals['price_per_oz']
    aisc          = vals['aisc']
    exchange_rate = vals['exchange_rate']
    shrs_out      = vals['shrs_out']
    pe            = vals['pe']

    share_price = (((oz_per_yr * (price_per_oz - aisc)) * exchange_rate) /shrs_out) * pe

    return share_price

print(share_price_calc(values))
