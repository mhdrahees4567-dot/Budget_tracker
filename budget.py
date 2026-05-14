from data import load_data, save_data   


def add_income():
        
    data = load_data()
    amount = float(input("Enter income amount: "))
    data['income']+= amount
    
    save_data(data)
    print('Income added successfully')
    
def add_expense():
    
    data=load_data()
    category=input('Enter expense category: ')
    amount=float(input('Enter expense amount:'))
    
    expence={'category':category,'amount':amount}
    data['expenses'].append(expence)
    save_data(data)

    print("Expense added successfully.")


def view_summary():
    
    
    data=load_data()
    total_income=data['income']
    total_expenses=sum(expense['amount'] for expense in data['expenses'])
    balance=total_income-total_expenses
    
    print(f"Total Income   : {total_income}")
    print(f"Total Expense  : {total_expenses}")
    print(f'Remaining Bal. : {balance}')
    
    print("\nExpense Details:")

    for item in data["expenses"]:
        
        
        print(f"{item['category']} --> {item['amount']}")