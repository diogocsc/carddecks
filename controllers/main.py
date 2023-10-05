import json
from odoo import http
from odoo.http import request, Response


#class Cards(http.Controller):
#    @http.route("/cards")
#    def list(self, **kwargs):
#        Card = http.request.env["carddecks.card"]
#        cards = Card.search([])
#        return http.request.render(
#            "carddecks.card_list_template",
#            {"cards": cards}
#        )


# from https://www.odoo.com/pt_BR/forum/ajuda-1/how-to-call-json-web-services-in-the-odoo-to-push-the-data-to-another-application-153675
class MyApiClass(http.Controller):

    @http.route("/cards", auth='public', type='http', methods=['GET'], cors='*')
    def get_api_method(self, **kw):
        Card = http.request.env['carddecks.card']
        deck_name = kw.get("deck")
        cards = Card.sudo().search_read([("deck.name", "=", deck_name)], ['cardText', 'url'])

        headers = {'Content-Type': 'application/json'}
        body = {'results': {'code': 200, 'message': cards}}

        return Response(json.dumps(cards, default=str), headers=headers)

    @http.route("/cards", auth='none', type='http', methods=['POST'], csrf=False, cors='*')
    def post_api_method(self, cardText, **kw):
        Card = http.request.env['carddecks.card']
        cards = Card.sudo().search_read([("cardText", "=", cardText)], ['cardText', 'url'])

        headers = {'Content-Type': 'application/json'}
        body = {'results': {'code': 200, 'message': partners}}

        return Response(json.dumps(body), headers=headers)
