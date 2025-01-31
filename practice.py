class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, account, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer
        bank        the name of the bank
        account     the account identifier
        limit       credit limit
        """
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return the name of the customer"""
        return self._customer

    def get_bank(self):
        """Return th banks name"""
        return self._bank

    def get_account(self):
        """return the card identu=ifying number(typically stored as string)"""
        return self._account
