
#Name: Avnish Sengupta
#Discussion: 1B
#Homework Submission 2
 
def rpsComputerCheat(playerChoice):
    '''A version of rock-paper-scissors where the computer always wins.'''
    if playerChoice in ('rock','scissors', 'paper'):
        return "Computer wins!"
    else:
        return "Invalid input!"



# tests for rpsComputerCheat
def test_rpsComputerCheat():
    assert(rpsComputerCheat('rock') == 'Computer wins!')
    assert(rpsComputerCheat('scissors')== 'Computer wins!')
    assert(rpsComputerCheat('paper')=='Computer wins!')
    assert(rpsComputerCheat('lizard')=='Invalid input!')


def rpsComputerRock(playerChoice):
    '''A version of rock-paper-scissors where the computer always chooses rock.'''
    ComputerChoice= "rock"
    if playerChoice=='rock':
        return "Tie game!"
    elif playerChoice=='scissors':
        return "Computer wins!"
    elif playerChoice=='paper':
        return "Player wins!"
    else:
        return "Invalid input!"

def test_rpsComputerRock():
    assert(rpsComputerRock('rock')== 'Tie game!')
    assert(rpsComputerRock('scissors')=='Computer wins!')
    assert(rpsComputerRock('paper')=='Player wins!')
    assert(rpsComputerRock('spock')== 'Invalid input!')
        


# add a function to test the above function!



def rps(playerChoice, computerChoice):
    '''A version of rock-paper-scissors for two players.'''
    if computerChoice=="rock":
        if playerChoice=="rock":
            return rpsComputerRock("rock")
        elif playerChoice=="paper":
            return rpsComputerRock("paper")
        elif playerChoice=="scissors":
            return rpsComputerRock("scissors")
        else:
            return rpsComputerRock("lizard")
    elif computerChoice== "paper":
        if playerChoice== "paper":
            return "Tie game!"
        elif playerChoice== "scissors":
            return "Player wins!"
        elif playerChoice=="rock":
            return "Computer wins!"
        else:
            return "Invalid input!"
    elif computerChoice== "scissors":
        if playerChoice=="scissors":
            return "Tie game!"
        elif playerChoice== "paper":
            return "Computer wins!"
        elif playerChoice=="rock":
            return "Player wins!"
        else:
            return "Invalid input!"
    else:
        return "Invalid input!"

def test_rps():
    assert(rps("rock","rock")=="Tie game!")
    assert(rps("rock","paper")=="Computer wins!")
    assert(rps("rock","scissors")=="Player wins!")
    assert(rps("rock", "spock")=="Invalid input!")
    assert(rps("paper","rock")=="Player wins!")
    assert(rps("scissors","rock")=="Computer wins!")
    assert(rps("scissors","scissors")=="Tie game!")
    assert(rps("scissors","paper")== "Player wins!")
    assert(rps("scissors","lizard")== "Invalid input!")
    assert(rps("paper","scissors")=="Computer wins!")
    assert(rps("paper", "paper")=="Tie game!")
    assert(rps("paper", "joker")=="Invalid input!")

# add a function to test the above function!


def fizzBuzz(n):
    '''A player for the game fizz buzz.'''
    if n%15==0:
        return "FizzBuzz!"
    elif n%5==0:
        return "Buzz!"
    elif n%3==0:
        return "Fizz!"
    else:
        return n

def test_fizzBuzz():
    assert(fizzBuzz(2)==2)
    assert(fizzBuzz(105)=="FizzBuzz!")
    assert(fizzBuzz(-120)=="FizzBuzz!")
    assert(fizzBuzz(-33)=="Fizz!")
    assert(fizzBuzz(-20)=="Buzz!")
    
    


# add a function to test the above function!


def deposit(amount, savings, accounts):
    '''Deposits amount dollars in a bank account.

       The argument savings is a boolean indicating whether to deposit
       into the savings (True) or checking (False) account.
       
       The argument accounts is a two-element list of numbers,
       representing respectively the amount of money in a user's savings and
       checking accounts.

       The function returns a list representing the new account balances.'''
    if amount==str(amount) or (savings!=True and savings!=False) or accounts[0]==str(accounts[0]) or accounts[1]==str(accounts[1]):
        return "Invalid input!"
    elif savings==True:
        return [accounts[0]+amount, accounts[1]]
    elif savings==False:
        return [accounts[0],accounts[1]+amount]
    else:
        return "Invalid input!"

def test_deposit():
    assert(deposit(5,True,[34,12])==[39,12])
    assert(deposit(0,False,[77,11])==[77,11])
    assert(deposit(-33,True,[94,-33])==[61,-33])
    assert(deposit(90,False,[67,"fruit"])=="Invalid input!")
    
           

# add a function to test the above function!


def withdraw(amount, savings, accounts):
    '''Withdraws amount dollars from a bank account.

       The argument savings is a boolean indicating whether to withdraw
       from the savings (True) or checking (False) account.
       
       The argument accounts is a two-element list of numbers,
       representing respectively the amount of money in a user's savings and
       checking accounts.

       No money is withdrawn if there are insufficient funds in the selected
       account.

       The function returns a list representing the new account balances.'''

    if amount==str(amount) or (savings!=True and savings!=False) or accounts[0]==str(accounts[0]) or accounts[1]==str(accounts[1]):
        return "Invalid input!"
    elif (savings==False and accounts[1]<amount) or (savings==True and accounts[0]<amount):
        return [accounts[0],accounts[1]]
    elif savings==True:
        return [accounts[0]-amount,accounts[1]]
    elif savings==False:
        return [accounts[0],accounts[1]-amount]
    else:
        return "Invalid input!"

    
    

def test_withdraw():
    assert(withdraw(23,True,[90,66])==[67,66])
    assert(withdraw(34,False,[35,36])==[35,2])
    assert(withdraw(90,True,[66,85])==[66,85])
    assert(withdraw(90,False,[67,"fruit"])=="Invalid input!")
    

# add a function to test the above function!
