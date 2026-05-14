from budget import add_income, add_expense, view_summary

def main():
    while True:
        print("\nPersonal Budget Tracker")
        print('1. Add Income')
        print("2. Add Expense") 
        print("3. View Summary")
        print("4. Exit")
        
        choice = input('Select an option: ')
        
        
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()   
        elif choice == '3':
            
            view_summary()
        elif choice == '4':
            print("Exiting the budget tracker. Goodbye")
            break
        else:
            
            print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()