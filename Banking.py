# instanve variable:name,amount,adress,acc.no
#instace methods:create acoount,display account info
# class variable=bank name,roi on fd
# clss method:disply bank inf
# static method:kyc

class Bank_Account:

    Bank_name="HDFC Bank Pvt Ltd"
    ROI_on_FD=6.7


    def __init__(self,):
        self.Name=""
        self.Amount=0
        self.Adress=""
        self.AccountNo=0

    def CreateAccount(self):
        print("Enter your Name:")
        self.Name=input()

        print("Enter your inital amount:")
        self.Amount = int(input())

        print("Enter your Address:")
        self.Adress = input()

        print("Enter your Account no:")
        self.AccountNo = int(input())

    def DisplayaccountInfo(self):
        print("****************Your Account Info as Below*******************")
        print("Name of Account Holder:",self.Name)
        print("Account no:", self.AccountNo)
        print("Address of Account Holder:", self.Adress)
        print("Current Amount of Account Holder:", self.Amount)

    @classmethod
    def DisplayBankInfo(Cls):
        print("Welcome to Banking Console")
        print("Name of bank:",Cls.Bank_name)
        print("rate of intest:",Cls.ROI_on_FD)

    @staticmethod
    def DisplayKYCinfo():
        print("Please consider below kyc info")
        print("Accourding to the rule of govt of india submit beloe")
        print("1:Clear and recent passport size pic")
        print("2:Photo of adharcard")
        print("3:photo of Pan card")

    def Deposit(self,value):
        self.Amount=self.Amount+value
        #return self.Amount

    def Withdraw(self,value):
        self.Amount=self.Amount-value
        #return self.Amount



def main():
    print("**********Banking Application***********************************")
    print("--------------------------------------------------------------")
    print("**********Calling Sataic method to disply KYC details*************")
    Bank_Account.DisplayKYCinfo()

    #print("Name of Bank:",Bank_Account.Bank_name)
    #print("Rate of intrst on FD:",Bank_Account.ROI_on_FD)

    print("**********calling class method*************")
    Bank_Account.DisplayBankInfo()

    print("**********creating class object*************")
    user1=Bank_Account()
    user2=Bank_Account()

    print("Creating fisrt Account")
    user1.CreateAccount()

    print("Creating second Account")
    user2.CreateAccount()

    print("**********Calling Instance methods*************")
    user1.DisplayaccountInfo()
    user2.DisplayaccountInfo()

    user1.Deposit(500)
    print("Amount of {} after deposit is {}:".format(user1.Name,user1.Amount))


    user2.Deposit(1200)
    print("Amount of {} after deposit is {}:".format(user2.Name,user2.Amount))

    user1.Withdraw(200)
    print("Amount of {} after withdrw is {}:". format(user1.Name,user1.Amount))
    user2.Withdraw(700)
    print("Amount of {} after withdrw is {}:". format(user2.Name,user2.Amount))

    print("----------------------------------------------------------------")
    print("---------- End of banking appplication ----------")
    print("----------------------------------------------------------------")

if __name__=="__main__":
    main()