# Budget App

Full code run with examples test can be found in: https://replit.com/@tiagoreboucas90/boilerplate-budget-app#budget.py

The `Category` class in `budget.py` is able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class has an instance variable called `ledger` that is a list. The class also contains the following methods:

- A `deposit()` method that accepts an amount and description. If no description is given, the default is an empty string. The method appends an object to the ledger list in the form of `{"amount": amount, "description": description}`.
- A `withdraw()` method that is similar to the `deposit()` method, but the amount passed in is stored in the ledger as a negative number. If there are not enough funds, nothing is added to the ledger. This method returns `True` if the withdrawal took place, and `False` otherwise.
- A `get_balance()` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
- A `transfer()` method that accepts an amount and another budget category as arguments. The method adds a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing is added to either ledgers. This method returns `True` if the transfer took place, and `False` otherwise.
- A `check_funds()` method that accepts an amount as an argument. It returns `False` if the amount is greater than the balance of the budget category and returns `True` otherwise. This method is used by both the `withdraw()` and `transfer()` methods.

When the budget object is printed, the output is as the example bellow:

```text
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Besides the `Category` class, there is a function (outside of the class) called `create_spend_chart()` that takes a list of categories as an argument. It returns a bar chart.

The chart shows the percentage spent in each category passed in to the function. The percentage spent is calculated only with withdrawals and not with deposits. Down the left side of the chart there are percentage labels 0 - 100. The "bars" in the bar chart is made out of the "o" character. The height of each "bar" is rounded down to the nearest 10. Each category name is written vertically below the bar. There is a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Bellow is an example aoutput:

```text
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

## Testing
- If you chose to open in [replit](https://replit.com/@tiagoreboucas90/boilerplate-budget-app#budget.py), the code is writen in `budget.py`. For development, you can use `main.py` to test the `Category` class. Click the "run" button and `main.py` will run.
- We imported the tests from `test_module.py` to `main.py` for your convenience. The tests will run automatically whenever you hit the "run" button.
