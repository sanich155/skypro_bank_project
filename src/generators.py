def filter_by_currency(transactions_list, currency):
    """Генерирует по одной транзакции в соответствующей валюте из списка"""

    for transaction in transactions_list:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction

def card_number_generator(start: int, stop: int) -> int:
    """Генерирует по очереди номера карт в указанном диапазоне"""
    for num in range(start, stop + 1):
        yield num

def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction['description']
