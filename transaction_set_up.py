''' Creating Finite State Machine to process debit or credit transactions '''
from transaction_fsm import StateMachine

def start_state(txt, account):
    ''' Define start state'''
    if 'Debit' in txt:
        new_state = "debit_state"
    elif 'Credit' in txt:
        new_state = "credit_state"
    else:
        new_state = "error_state"
    return (new_state, txt, account)

def debit_state_transition(txt, account):
    '''Define state transition'''
    split_txt = txt.split(':')
    name = split_txt[0]
    num = int(split_txt[1])

    account.process_debit(num, name)
    new_state = 'Start'
    account.print_balance()

    return (new_state, txt, account)

def credit_state_transition(txt, account):
    '''Define credit state transition'''
    split_txt = txt.split(':')
    name = split_txt[0]
    num = int(split_txt[1])

    account.process_credit(num, name)
    account.print_balance()

    if account.get_balance() <= -1000:
        new_state = 'end_state'
        account.print_transactions()
    else:
        new_state = 'Start'

    return (new_state, txt, account)

if __name__== "__main__":
    m = StateMachine()
    m.add_state("Start", start_state)
    m.add_state("debit_state", debit_state_transition)
    m.add_state("credit_state", credit_state_transition)
    m.add_state("error_state", None, end_state=1)
    m.add_state('end_state',None, end_state=1)
    m.set_start("Start")
    m.run()
