#! /usr/bin/env python
# -*- coding: utf-8 -*-

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    models = []
    for mfg, modellist in cars.items():
        first = modellist[0]
        models.append(first)
    return models


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matches = []
    for mfg, modellist in cars.items():
        for model in modellist:
            if grep.casefold() in model.casefold():
                matches.append(model)
    return sorted(matches)


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    for mfg, modellist in cars.items():
        cars[mfg] = sorted(modellist)
    return cars
