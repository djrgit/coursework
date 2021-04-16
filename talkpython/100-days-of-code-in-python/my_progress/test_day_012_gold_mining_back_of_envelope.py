#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from day_012_gold_mining_back_of_envelope import share_price_calc


class FakeData:

    def __init__(self, oz_per_yr=100000, price_per_oz=1750,
                 aisc=900, exchange_rate=1.25, shrs_out=146250000,
                 pe=10):
        self.oz_per_yr     = oz_per_yr
        self.price_per_oz  = price_per_oz
        self.aisc          = aisc
        self.exchange_rate = exchange_rate
        self.shrs_out      = shrs_out
        self.pe            = pe


@pytest.fixture
def result():
    def apply(oz_per_yr=100000, price_per_oz=1750, aisc=900, 
              exchange_rate=1.25, shrs_out=146250000, pe=10):
        return FakeData(oz_per_yr=oz_per_yr,
                        price_per_oz=price_per_oz,
                        aisc=aisc,
                        exchange_rate=exchange_rate,
                        shrs_out=shrs_out,
                        pe=pe)

    v = apply()

    vals = {
        'oz_per_yr':     v.oz_per_yr,
        'price_per_oz':  v.price_per_oz,
        'aisc':          v.aisc,
        'exchange_rate': v.exchange_rate,
        'shrs_out':      v.shrs_out,
        'pe':            v.pe
    }

    return vals


def test_share_price_calc_value(result):
    value = share_price_calc(result)
    assert value == 7.264957264957265

