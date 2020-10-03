''' Creating Finite State Machine to process debit or credit transactions '''
from account import Account
from transactionFsm import StateMachine

def start_state(txt, account):
    if 'Debit' in txt:
        newState = "debit_state"
    elif 'Credit' in txt:
        newState = "credit_state"
    else:
        newState = "error_state"
    return (newState, txt, account)

def debit_state_transition(txt, account):
    split_txt = txt.split(':')
    name = split_txt[0]
    num = int(split_txt[1])
    account.process_debit(num, name)
    newState = 'Start'
    account.print_balance()
    return (newState, txt, account)

def credit_state_transition(txt, account):
    split_txt = txt.split(':')
    name = split_txt[0]
    num = int(split_txt[1])
    account.process_credit(num, name)
    account.print_balance()

    if account.get_balance() <= -1000:
        newState = 'end_state'
        account.print_transactions()
    else:
        newState = 'Start'
    return (newState, txt, account)

if __name__== "__main__":
    m = StateMachine()
    m.add_state("Start", start_state)
    m.add_state("debit_state", debit_state_transition)
    m.add_state("credit_state", credit_state_transition)
    m.add_state("error_state", None, end_state=1)
    m.add_state('end_state',None, end_state=1)
    m.set_start("Start")
    m.run()
