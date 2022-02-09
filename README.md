# Implementation of State Machines on Bank Transactions

That code is an implementation of Finite State Machines concept and applied to banking transactions
In this scenario user inputs either Debit or Credit transaction with it's value

The error state is anything that is not debit or credit
the end state is reached once user account balance is <= -1000

- Account keeps track of balance and transactions
- transactionFsm imolements Finite State Machine
- transactionSetUp runs the application

## Requirements

[Python3](https://www.python.org/downloads/) v3.9.6

## How to run

```
python3 transaction_set_up.py
```

#### Resources

[FSM sample implementation](https://www.python-course.eu/finite_state_machine.php)

