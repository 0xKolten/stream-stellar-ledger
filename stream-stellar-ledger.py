import json
from stellar_base.horizon import Horizon

def data_handler(response):
    # Filter "hello" response  
    if response.__dict__['data'] != '"hello"':
        # Convert 'data' JSON string to Python object
        ledger_data = json.loads(response.__dict__['data'])  
        print("Ledger:", ledger_data['sequence'])
        print("Successful Transactions:", ledger_data['successful_transaction_count'])
        print("Failed Transactions:", ledger_data['failed_transaction_count'])
        print("Total Operations:", ledger_data['operation_count'], '\n')

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
