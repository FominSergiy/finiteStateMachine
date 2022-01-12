'''state machine setup'''
from account import Account

class StateMachine:
    '''Class defines a state machine'''
    def __init__(self):
        self.handlers = {}
        self.start_state = None
        self.end_state = []

    def add_state(self, name, handler, end_state=0):
        '''Add a state to the state machine'''
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.end_state.append(name)

    def set_start(self, name):
        '''Define the start state'''
        self.start_state = name.upper()

    def run(self):
        '''Run the state machine'''
        account = Account()
        try:
            handler = self.handlers[self.start_state]
        except:
            raise Exception("must call .set_start() before .run()")
        if not self.end_state:
            raise Exception("at least one state must be an end_state")

        while True:
            if handler == self.handlers[self.start_state]:
                debit = 'Debit:100'
                credit = 'Credit:200'
                cargo = input(f'Input yourtransaction (ex = {debit} or {credit}): ')

            (new_state, cargo, account) = handler(cargo, account)

            if new_state.upper() in self.end_state:
                print("reached", new_state)
                break
            else:
                handler = self.handlers[new_state.upper()]
