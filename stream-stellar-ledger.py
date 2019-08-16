import json
from stellar_base.horizon import Horizon

def data_handler(response):
    # Print relevant data 
    print("Ledger:", response['sequence'])
    print("Successful Transactions:", response['successful_transaction_count'])
    print("Failed Transactions:", response['failed_transaction_count'])
    print("Total Operations:", response['operation_count'], '\n')

def get_ledger_data():
    # Create Horizon object 
    ledger_data = Horizon(horizon_uri='https://horizon.stellar.org')
    # Start streaming from ledgers endpoint 
    ledger_data = ledger_data.ledgers(cursor='now', order='asc', sse=True)
    # Handle responses 
    for ledger in ledger_data:
        data_handler(ledger)

if __name__ == '__main__':
    get_ledger_data()
