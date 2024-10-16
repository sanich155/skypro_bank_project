def filter_by_state(transactions: list, state: str = "EXECUTED") -> list:
    """Оставляет транзакции с указанным статусом выполнения.
    По умолчанию - выполненные"""

    result_transactions = []
    for transaction in transactions:
        if "state" not in transaction.keys():
            continue
        if transaction["state"] == state:
            result_transactions.append(transaction)
    return result_transactions


def sort_by_date(transactions: list, sort_direction: bool = True) -> list:
    """Сортирует транзакции по дате выполнения"""

    transactions.sort(key=lambda transaction: transaction["date"], reverse=sort_direction)
    return transactions


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ],
        sort_direction=False,
    )
)
