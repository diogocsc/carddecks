# -*- coding: utf-8 -*-
{
    'name' : 'Card Decks',
    'version' : '16.0.0.0.1',
    "author": "Diogo Cordeiro",
    'summary': 'Playable Card Decks',
    'sequence': 10,
    'description': """
Playable Card Decks
===================
With this module you can configure decks of cards and play them

    """,
    'category': 'Services/Card Decks',
    'website': 'https://github.com/diogocsc/carddecks',
    'depends' : ["base"],
    'data': [
        'security/carddecks_security.xml',
        'security/ir.model.access.csv',
        'views/carddecks_menu.xml',
        'views/card_view.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'license': 'AGPL-3',
}
