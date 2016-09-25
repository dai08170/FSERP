from FSERP import client
from trytond.transaction import Transaction
from FERP.cleint.authentication import Authentication


class Admin(object):
    def __init__(self):
        self.restaurant = None

    def get_restaurant(self):
        if not self.restaurant:
            with Transaction().start(client.DB_NAME, Authentication().get_admin()) as transaction:
                party_module = client.pool.get('party.party')
                self.restaurant = party_module.search([('code', '=', 0)])
        return self.restaurant


    def set_restaurant(self, values={}):
        if not self.restaurant:
            with Transaction().start(client.DB_NAME, Authentication().get_admin()) as transaction:
                party_module = client.pool.get('party.party')
                values['code'] = 0;
                self.restaurant, = party_module.create([values])
        return self.restaurant


    def upate_restaurant(self, values):
        pass  # TODO