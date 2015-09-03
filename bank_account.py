""" Bank Account"""
import os

RETVAL = os.getcwd()

print "\n\nDirectory changed successfully %s \n"% RETVAL

class BankAccount:
    ''' class '''
    def __init__(self, name, balance, password):
        self.balance = balance
        self.name = name
        self.password = password

    def logwrite(self):
        ''' creates a log file '''
        log = open(os.getcwd() + "%s-log" % self.name, 'a')
        log.write(RECORD)
        log.close()

    def writebalance(self):
        ''' update the file '''
        account = open(os.getcwd() + "%s", "w")
        account.write("Name %s Balance %d Password %s"%(self.name, self.balance, self.password))
        account.close()


    def identify(self):
        '''Identifies the user'''
        global ACCESS
        ACCESS = 0
        while ACCESS != 1:
            prompt = raw_input("Password:")
            if prompt != self.password:
                print "Incorrect."
            if prompt == self.password:
                print "Correct.\nYou may proceed."
                ACCESS += 1


    def current_balance(self):
        '''Displays the current balance'''

        print "Display Current Balance"
        print "Current Balance: $%d" % int(self.balance)
        self.main_menu()

    def withdraw(self):
        '''Withdraws money from current bank account'''
        print "access"
        print "Withdraw Money"
        withdrawal = raw_input("Type the balance to withdraw:")
        self.balance = int(self.balance) - int(withdrawal)
        global RECORD
        RECORD = "Withdraw%d from%s\nCurrentBalnce:%d\n"%(int(withdrawal), self.name, self.balance)
        self.logwrite()
        self.writebalance()
        print "Current Balance:$%d"% int(self.balance)

    def deposit(self):
        '''Deposits money in the current bank account'''
        print "Deposit Money"
        deposit = int(raw_input("Type the amount to deposit:"))
        self.balance = int(self.balance) + int(deposit)
        global RECORD
        RECORD = "Deposited %d to%s\nCurrent Balance:%d\n"%(int(deposit), self.name, self.balance)
        self.logwrite()
        self.writebalance()
        print "Current Balance:%d"% self.balance

    def transfer(self):
        '''Transfers money between accounts'''
        print "Transfer Money Between Accounts"
        ammount = int(raw_input("Type the ammount to transfer:"))
        receiver = (raw_input("Type the name of the account to transfer to:"))
        self.balance = int(self.balance) - int(ammount)
        receiver.balance = int(receiver.balance)+ int(ammount)
        global RECORD
        RECORD = "%d transferred to%s\nCurrentBalance:%d\n" %(ammount, receiver.name, self.balance)
        self.logwrite()
        self.writebalance()
        print "Current Balance:$%d" % self.balance



    def login(self):
        ''' login from existing account '''
        print "Login"
        global ACCOUNT_NAME
        ACCOUNT_NAME = raw_input("Account Name: ")
        self.identify()
        self.user_cp()

    def create_account(self):
        '''Creates Account'''
        acct_name = raw_input("Name of new account: ")
        acct_balance = int(raw_input("How much do you wish to deposit? "))
        acct_pass = raw_input("Type a password for your new account: ")
        create = open(os.getcwd() + "%s" % self.name, "w")
        create.write("Name %s\n Balance %d\n Password %s"%(acct_name, acct_balance, acct_pass))
        create.close()
        self.current_balance()

    def readlogs(self):
        '''Reads logs'''
        log = open(os.getcwd() + "%s-log"% self.name, "r")
        print log.read()
        log.close()

    def main_menu(self):
        '''The Main Menu'''
        print "What Do You Want To Do.? \n"
        print "                    Create Account \n "
        print "Current Balance        With Draw        Deposit \n"
        print "             Transfer            Login \n"
        print "                       Main Menu"
        action = raw_input("> ")
        if action == "create account":
            self.create_account()

        elif action == "login":
            self.login()

        elif action == "current balance":
            self.current_balance()

        elif action == "deposit":
            self.deposit()

        elif action == "with draw":
            self.withdraw()

        elif action == "transfer":
            self.transfer()

        elif action == "main menu":
            self.main_menu()

        elif action == "read logs":
            self.readlogs()

    def user_cp(self):
        '''User Control Panel'''
        print "Welcome to pybank %s"%ACCOUNT_NAME
        print "Current Balance:%d \n" % self.balance
        self.main_menu()


print "\n                Welcome to pybank\n \n"
print "Type 'accounts' And Then Your Account Name To Proceed \n \n OR \n"
print "Type 'create account' To Create New Account \n"
ABC = raw_input("> ")

if ABC == 'create account':
    A = 'Name'
    B = 'Balance'
    C = 'Password'
    INSTANCE = BankAccount(A, B, C)
    INSTANCE.create_account()

elif ABC == "accounts":
    ACCT = raw_input("Enter Your Account Name: ")
    FILEDIR = os.getcwd()
    READ_LINE = open(ACCT, 'r')
    CHECK = str(READ_LINE.read())
    NAME = CHECK.find('Name')
    BALANCE = CHECK.find('Balance')
    PASSWORD = CHECK.find('Password')
    INSTANCE = BankAccount(NAME, BALANCE, PASSWORD)
    INSTANCE.main_menu()

else:
    print "You Enter Wrong Text"

