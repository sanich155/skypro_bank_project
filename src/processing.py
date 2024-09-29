def filter_by_state(transactions: list, state='EXECUTED') -> list:
    """ Оставляет транзакции с указанным статусом выполнения.
     По умолчанию - выполненные """

    result_transactions = []
    for transaction in transactions:
        if transaction['state'] == state:
            result_transactions.append(transaction)
    return result_transactions


def sort_by_date(transactions: list, sort_direction=True) -> list:
    """ Сортирует транзакции по дате выполнения """

    for i in range(len(transactions)):
        result_transactions = []
        earliest_tran = transactions[0]
        for transaction in transactions:
            if transaction['date'] < earliest_tran['date']:
                earliest_tran = transaction
        result_transactions.append(earliest_tran)
        transactions.remove(transaction)
    if sort_direction:
        return result_transactions
    else:
        return reversed(result_transactions)


test_list_1 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
test_list_2 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(test_list_1, 'EXECUTED'))

print(sort_by_date(test_list_2))
