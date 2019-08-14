import json
from stellar_base.horizon import Horizon

def data_handler(response):
    if response.__dict__['data'] != '"hello"':
        ledger_data = json.loads(response.__dict__['data'])
        print("Ledger:", ledger_data['sequence'])
        print("Successful Transactions:", ledger_data['successful_transaction_count'])
        print("Failed Transactions:", ledger_data['failed_transaction_count'])
        print("Total Operations:", ledger_data['operation_count'], '\n')

def show_data():
    ledger_data = Horizon(horizon_uri='https://horizon.stellar.org')
    ledger_data = ledger_data.ledgers(cursor='now', order='asc', sse=True)
    for ledger in ledger_data:
        data_handler(ledger)

if __name__ == '__main__':
    show_data()
