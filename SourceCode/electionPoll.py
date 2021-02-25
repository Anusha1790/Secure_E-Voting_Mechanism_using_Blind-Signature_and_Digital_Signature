import BlindSig as bs
import _thread
import time
import os
import hashlib
import random
yell = '\u001b[33;1m'
reset = '\u001b[0m'
              



class poll:
    def __init__(self):
        self.signer = bs.Signer()
        self.publicKey = self.signer.getPublicKey()
        self.n = self.publicKey['n']
        self.e = self.publicKey['e']
        
    def poll_response(self, poll_answer, eligble_answer):
       
       if (eligble_answer == 0):
            eligble_answer = "n";
       elif (eligble_answer == 1):
            eligble_answer = "y";
       
    
       print('\n\n')
       for i in range(200):
            print("-", end="")
       print()    
       for i in range(100):
            print(" ", end="")
       print("\u001b[31mMODULE 2\u001b[37m")
       for i in range(200):
            print("-", end="")
       print('\n\n')    
       print("\u001b[32;1m2. Voter Prepares Ballot for getting signed by Signing Authority:\u001b[0m", end='\n\n')
       print()
       print("\u001b[35;1m(a) Generates random x such that 1<=x<=n\u001b[0m", end='\n\n') 
       x = random.randint(1,self.n)
       print("\u001b[33;1mx: \u001b[0m", x, end="\n\n")
    
       print("\u001b[35;1m(b) Voter chooses favorite candidate, option, etc. on ballot\u001b[0m", end='\n\n')
       message = poll_answer
       print("\u001b[33;1mpoll_answer: \u001b[0m", poll_answer, end="\n\n")
       print("\u001b[35;1m(c) Creates (concatenating) message: poll_answer + x and produces it's hash\u001b[0m", end='\n\n')
       concat_message = str(message) + str(x)
       print("\u001b[33;1mConcatenated message: \u001b[0m", concat_message, end="\n\n") 
       message_hash = hashlib.sha256(concat_message.encode('utf-8')).hexdigest()
       message_hash = int(message_hash,16)
       print("\u001b[33;1mhash(concatenated_message), m= \u001b[0m", message_hash, end="\n\n")
       voter = bs.Voter(self.n, eligble_answer)
    
       blindMessage = voter.blindMessage(message_hash, self.n, self.e)
       if eligble_answer==1 : 
          print("\u001b[33;1mBlinded message: \u001b[0m" + str(blindMessage))
       print()
       
       print("\u001b[35;1m(f) Sends m'(blinded message) to signing authority\u001b[0m")
       signedBlindMessage = self.signer.signMessage(blindMessage, voter.getEligibility())
 
       if signedBlindMessage == None:
           print("\u001b[31;1mINELIGIBLE VOTER....VOTE NOT AUTHORIZED!\u001b[0m")
       else:
           print("\u001b[33;1mSigned blinded message: \u001b[0m" + str(signedBlindMessage))
           print()
           signedMessage = voter.unwrapSignature(signedBlindMessage, self.n)
          
           print('\n\n')
           for i in range(200):
              print("-", end="")
           print()    
           for i in range(100):
              print(" ", end="")
            
            
            
           
           print("\u001b[31mMODULE 5\u001b[37m")
           for i in range(200):
              print("-", end="")
           print('\n\n')
            
           print("\u001b[32;1m5. Ballot Received, Verified, and Counted\u001b[0m", end='\n\n')
           print("A voter's vote in the ballot shall consist of the following: ")
           print()
           print("(a) His vote concatened with a number x : ",concat_message)
           print()
           print("(b) The hash of his concatenated vote signed by authority which is basically the hashed message encrypted with signing authority's private key (m^d)%n : ",signedMessage)
           print()
           verificationStatus, decoded_message = bs.verifySignature(message, x ,signedMessage, self.e, self.n)
        
           print("Verification status: " + str(verificationStatus))
           if(verificationStatus==True):
               print("Since the verification is true, Hence the vote is the first digit of the concatenated message: ", decoded_message)
                
    
       
class poll_machine:
    
    def __init__(self):
        self.p = poll()
        print("\u001b[32;1mEnter your choice\u001b[0m")
        print()
        print("(1) Apple     (2) Ball      (3) Rat      (4) Avengers    (5) Elephant")
        n=int(input())
        print()
        
        while n<1 or n>5:
            print("\u001b[31;1mInput",n, "is not a valid option. Please enter a valid option:\u001b[0m")
            n=int(input())
            print()
        print()

        print("\u001b[32;1mAre you above 18?\u001b[0m", end="\n\n")
        print("(0) No     (1) Yes", end="\n")
        a=int(input())
        if a==1:
            print("\u001b[32;1mVoter Eligible\u001b[0m")
        self.p.poll_response(n,a)
    
pm = poll_machine()



    







