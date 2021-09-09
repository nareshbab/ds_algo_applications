class CreditCard:
    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """
        Creates a new instance of Credit Card

        Args:
            customer: the name of the customer (eg: "Naresh" )
            bank: the name of the bank (eg: "SBI")
            acnt: the account identifier (eg: "123456")
            limit: credit limit of the card (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """

        Returns:
            the name of the customer
        """
        return self._customer

    def get_bank(self):
        """

        Returns:
            the name of the bank
        """
        return self._bank

    def get_account(self):
        """

        Returns:
            the account identifier
        """
        return self._account

    def get_limit(self):
        """

        Returns:
            the current credit limit of the card
        """
        return self._limit

    def get_balance(self):
        """

        Returns:
            the current balance of the card
        """
        return self._balance

    def charge(self, price):
        """

        Args:
            price: the amount to be charged on the card
        Returns:
            True if charge was processed; False if the charge was denied

        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """

        Args:
            amount:

        Returns:

        """
        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    """An extension to Credit card that compounds interest and fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        """
        Create a new Predatory credit card instance
        Args:
            customer: the name of the customer (eg: "Naresh" )
            bank: the name of the bank (eg: "SBI")
            acnt: the account identifier (eg: "123456")
            limit: credit limit of the card (measured in dollars)
            apr: annual percentage rate (eg: 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit
        Args:
            price:

        Returns:
            True, if charge was processed
            False, if charge is declined and charges $5 as a fee

        """

        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """Assess the monthly interest on the balance"""
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor