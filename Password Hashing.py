import hashlib
user={}
#sha256(password.encode('utf-8')).hexdigest()

def log_in(answer):
          if  answer in user :
              pa = input("Correct! Now type in your password: ")
              hash_object = hashlib.sha256(pa.encode())
              he = hash_object.hexdigest()
              if he == user[answer]:
                        print("Congrats you logged in")
              else:
                        print ("WRONG! YOU SHALL NOT PASS")
          else:
                    print("You have to sign up!" )
                    prompt()
def add_user(name):
          if name in user:
                    print("That name already exists! Sign in!")
                    prompt()
          else:
                    password = input("choose a password: ")
                    hash_object = hashlib.sha256(password.encode())
                    hex_dig = hash_object.hexdigest()
                    user [ name] = hex_dig


def prompt():
          choice = input ("Create new account or log in a different  account? Enter 'c' to create new account or enter 'l' to log in a different acconut. Type 'exit' to exit: ")
          if choice == 'c':
                    userName = input("Choose a username: " )
                    add_user(userName)
          elif choice == 'l':
                    answer = input("Username: ")
                    log_in(answer)
                    
          elif choice == 'exit':
                    print("BYEEE")
                    exit()
          elif choice != 'c' or choice != 'l' or choice != 'exit' :
                    print ("Y U STOOPID??? ONLY 'c' OR 'l' or 'exit'! UGH ")
                    prompt()
          
                    

while True:
	prompt()

