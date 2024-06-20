# necessary modules to work with
import random as  r
import time as t
import string as s

# this fucntion generates 6 dgit OTP kinda code for the confirmation of the payment of the student's fees
def give_code():
    N = 6
    res = ''.join(r.choices(s.ascii_uppercase +s.digits, k=N))
    return res
# this fucntion generates the 9 digit number which then gets passed to be later called a symbol number of the student
def sym_num():
    range_start = 10**(9-1)
    range_end = (10**9)-1
    return r.randint(range_start, range_end)
#  this function is responsible for generating a centre randomly as there is nothing specific to do with the exam centres but ill consider changing the centres as per the students Symbol number and their colleges later

def exam_center():
    centres=["Ambition college","patan Multiple campus",
            "Himalayan White house","KMC","GLobal ","Golden Gate",
            "LiverPool","Kings","Milestone","Texas"]
    return r.choice(centres)
# this ffunction assures the payment process of the studnents whose fees are yet to be paid will have to go through this process
# A payment process in short
def payment(std):
    print("_________________________________________________________________________________________")
    print('PAYMENT METHODS:\n')
    print("1.Cash\n")
    print("2.Card\n")
    print("3.Mobile banking\n")
    print("4.Crypto\n")
    x=input(">>")
    x=x.capitalize()
    match(x):
        case 'Cash':
            print("Submit the informed balance to the reception!!")
            print("Transaction...in process")
            for i in range(1,10):
                print("*"*i,"\n")
                t.sleep(r.uniform(0, 1))
            print("Transactioon complete")
            cod=give_code()
            print(f"Your Code Is :{cod}\n")
            x=input("Enter the code to start filing the form:\n")
            if(cod==x):
                print("valid Code!!")
                std=Exam_form()
            else:
                print("Invalid Code!!")
        case 'Card':
            print("Card Number must be equal to 16 Digits\n")
            card_num=input("Enter Your Card Number: \n")
            if(len(card_num)!=16):
                print("INVALID CARD NUMBER")
            else:
                print("For security purposes Enter the Expiration Date:\n")
                card_exp=input(">>")
                card_pin=input("Enter your Transaction Pin: \n")
                if(len(card_pin)!=6):
                    print("Invalid Pin Code")
                else:
                    act=input("Press Y for the Transaction confirmation:")
                    if(act.capitalize()=="Y"):
                        print("Transaction completed!")
                        cod=give_code()
                        print(f"Your Code Is :{cod}\n")
                        x=input("Enter the code to start filing the form:\n")
                        if(cod==x):
                            print("valid Code!!")
                            std=Exam_form()
                        else:
                            print("Invalid Code!!")
        case 'Mobile banking':
            print("OPTIONS:\n")
            print("ESEWA\nKHALTI")
            x=input(">>")
            if(x.capitalize()=="Esewa"):
                method=input("QR scan Or Phone Number input:\n>>")
                if(method.capitalize()=="Phonenumber"):
                    print("Please Send the Balance into this Mobile number : \n")
                    print("______________________________________________________________")
                    print("9825316449".center(50))
                    print("______________________________________________________________")
                    if_done=input("Press Done If the transfer of the Balance is complete :")
                    if(if_done):
                        cod=give_code()
                        print(f"Your Code Is :{cod}\n")
                        x=input("Enter the code to start filing the form:\n")
                        if(cod==x):
                            print("valid Code!!")
                            std=Exam_form()
                        else:
                            print("Invalid Code!!")
                elif(method.capitalize()=="Qr"):
                    print("Please scan this qr code")
                    #display a Qr code :
                    # use a image displayer to pop an image of a qr code
                    # to go further into the payment process
                    print("This feature is not yet available")
                    raise ("Not yet done ")
                else: print("Wrong input!")
        case 'Crypto':
            print("Match the following Crypto wallet code with your :")
            print("TGJDHS*&761284JHKJ")
            print("Press Done after the transaction is completed")
            trans_c=input(">>")
            if(trans_c.capitalize()=="Done"):
                cod=give_code()
                print(f"Your Code Is :{cod}\n")
                x=input("Enter the code to start filing the form:\n")
                if(cod==x):
                    print("valid Code!!")
                    std=Exam_form()
                else:
                    print("Invalid Code!!")
#  a class that defines the details of the student
class stud_deet:
    def __init__(self):
        self.name=input("Enter Name>>\n")
        self.address=input("Enter address>>\n")
        self.blud=input("Enter Blood Group>>\n")
        self.fees=input("Enter Y for the Fees paid>>\n")
        self.info()
    def info(self):
        print(f"Your Name is{self.name} from {self.address}")
        print(f"Your Blood group is {self.blud}")
        if(self.fees.capitalize()!="Y"):
            print("Your Fees are Not Paid")
            payment(self)
        else: 
            print("Your Exam fees are Paid proceed to fill the Exam form")
            self=Exam_form()


#  another class that deals with the registration of the student
class Exam_form:
    def __init__(self):
        self.reg_n=input("Enter Your Reg.No>>")
        self.symb=sym_num()
        self.Center=exam_center()
        self.inf()
    def inf(self):
        print(f"Your Registration Number is {self.reg_n}\n")
        print(f"Your symbol number is {self.symb} and your exam centre is {self.Center}")
        print("BEST OF LUCK FOR YOUR EXAMS!!")

# this section of code is for the number of student as there can be multiple students as a time
x=int(input("Enter the number of students :\n"))
x=97+x
for i in range(97,x):
    i=chr(i)
    i=stud_deet()
