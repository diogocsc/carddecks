# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Deck(models.Model):
    _name = "carddecks.deck"
    _description = "Deck"
    _inherit = "carddecks.imageurl"

    name = fields.Char(required=True, translate=True)
    cards = fields.One2many("carddecks.card", "deck", "Cards")
    description = fields.Char(translate=True)
    category = fields.Many2one('carddecks.category')
    total_cards = fields.Integer(compute="_compute_total_cards")
    url = fields.Char("Entry Card Image URL", help="Card that shows when we load the game for the first time")
    image = fields.Binary(string="Image", store=True, attachment=False)
    is_public = fields.Boolean(compute="_compute_is_public",
                               help="If True, the deck will be presented in the public website",
                               readonly=False,  # we can manually edit it
                               store=True)

    @api.depends("category.partner")
    def _compute_is_public(self):
        for deck in self:
            deck.is_public = not deck.category.partner

    def _compute_total_cards(self):
        for deck in self:
            deck.total_cards = len(deck.cards)

    @api.depends("url")
    @api.onchange('url')
    def _compute_image(self):
        for record in self:
            image = None
            if record.url:
                image = self.get_image_from_url(record.url)
            record.update({"image": image})