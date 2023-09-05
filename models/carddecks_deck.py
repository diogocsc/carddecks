# -*- coding: utf-8 -*-
from odoo import fields, models


class Deck(models.Model):
    _name = "carddecks.deck"
    _description = "Deck"
    name = fields.Char(required=True, translate=True)
    cards = fields.One2many("carddecks.card", "deck", "Cards")
    description = fields.Char(translate=True)
    category = fields.Many2one('carddecks.category')
    total_cards = fields.Integer(compute="_compute_total_cards")

    def _compute_total_cards(self):
        for deck in self:
            deck.total_cards = len(deck.cards)
