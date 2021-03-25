import BlindSig as bs
import hashlib
import random
import cryptomath
yell = '\u001b[33;1m'
reset = '\u001b[0m'
red = '\u001b[31m'
pink = '\u001b[35;1m'
              



class poll:
    def __init__(self):
        self.signer = bs.Signer()
        self.publicKey = self.signer.getPublicKey()
        self.n = self.publicKey['n']
        self.e = self.publicKey['e']
        
    def poll_response(self, poll_answer, eligble_answer):
       
       if (eligble_answer == 0):
            eligble_answer = "n"
       elif (eligble_answer == 1):
            eligble_answer = "y"
       
    
       print('\n\n')
       for i in range(100):
            print("-", end="")
       print()    
       for i in range(50):
            print(" ", end="")
       print("\u001b[31mMODULE 2\u001b[37m")
       for i in range(100):
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
           for i in range(100):
              print("-", end="")
           print()    
           for i in range(50):
              print(" ", end="")
            
            
            
           
           print("\u001b[31mMODULE 5\u001b[37m")
           for i in range(100):
              print("-", end="")
           print('\n\n')
            
           print("\u001b[32;1m5. Ballot Received and it's Verification \u001b[0m", end='\n\n')
           print("\u001b[35;1mA voter's vote in the ballot shall consist of the following: \u001b[0m", end='\n\n')
           print("\u001b[33;1m(a) His vote concatened with a number x: \u001b[0m",concat_message)
           print()
           print("\u001b[33;1m(b) The hash of his concatenated vote signed by authority which is basically the hashed message encrypted with signing authority's private key (m^d) mod n : \u001b[0m",signedMessage)
           print()
           verificationStatus, decoded_message = bs.verifySignature(message, x ,signedMessage, self.e, self.n)
           
           print()
           print("\u001b[33;1mVerification status: \u001b[0m" + str(verificationStatus), end="\n\n")
           if(verificationStatus==True):
               print("\u001b[35;1mSince the verification is true, Hence the vote is the first digit of the concatenated message: \u001b[0m", decoded_message, end='\n\n\n\n')
                
    
       
class poll_machine:
    
    def __init__(self):
        self.p = poll()
        print("\u001b[32;1mEnter your choice\u001b[0m")
        print()
        print("(1) Apple     (2) Ball      (3) Rat      (4) Avengers    (5) Elephant")
        poll_=int(input())
        print()
        
        while poll_<1 or poll_>5:
            print("\u001b[31;1mInput",poll_, "is not a valid option. Please enter a valid option:\u001b[0m")
            poll_=int(input())
            print()
        print()

        for i in range(100):
            print("-", end="")
        print()    
        for i in range(30):
            print(" ", end="")
        print("\u001b[31m Digital Signature Authentication \u001b[0m")
        for i in range(100):
            print("-", end="")
        print('\n\n')    


        print("\u001b[35;1m(a)Choose two large prime numbers p and q \u001b[0m",  end="\n\n")
        p = cryptomath.findPrime()
        print("\u001b[33;1m p: \u001b[0m", p,  end="\n\n")

        q = cryptomath.findPrime()
        print("\u001b[33;1m q: \u001b[0m", q,  end="\n\n")
        
        print("\u001b[35;1m(b)Calculate n=p*q \u001b[0m",  end="\n\n")
        n = p*q
        print("\u001b[33;1m n: \u001b[0m", n)
        print('\n')

        print("\u001b[35;1m(c)Calculate the totient of n \u001b[0m",  end="\n\n")
        phi = (p - 1)*(q - 1)
        print("\u001b[33;1m ϕ(n): \u001b[0m", phi, end="\n\n")

        print("\u001b[35;1m(d) Picks public_key such that gcd(ϕ(n),public_key)=1 & 1<public_key<ϕ(n):\u001b[0m", end='\n\n')

        foundEncryptionKey = False
        while not foundEncryptionKey:
            public_key = random.randint(2, phi - 1)
            if cryptomath.gcd(public_key, phi) == 1:
                foundEncryptionKey = True
        print("\u001b[33;1me: \u001b[0m", public_key, end='\n\n')

        print("\u001b[35;1m(e) Computes private_key, where private_key is the inverse of public_key modulo ϕ(n)\u001b[0m", end='\n\n')
        private_key = cryptomath.findModInverse(public_key, phi)     
        print("\u001b[33;1md: \u001b[0m",private_key, end='\n\n')

        print("\u001b[32;1mEnter id Number: \u001b[0m", end="\n\n")
        idNumber=int(input())
        concat_message = str(idNumber) 
        print("\n\n")

        print("\u001b[35;1m(f) Hash the message (here, message= idNumber) \u001b[0m",  end="\n\n")
        idNumber_hash = hashlib.sha256(concat_message.encode('utf-8')).hexdigest()
        idNumber_hash = int(idNumber_hash,16)
        print("\u001b[33;1mHash(idNumber): \u001b[0m", idNumber_hash, end="\n\n")

        print("\u001b[35;1m(g) Voter creates Digital Signature using s=(message_hash)^(private key)mod n \u001b[0m",  end="\n\n")
        s=pow(idNumber_hash, private_key, n) # ERR2
        print("\u001b[33;1mDigital Signature, s: \u001b[0m", s, end="\n\n")
        a=0

        ## verification:
        print("\u001b[35;1m(h) Digital Signature, s, and original message, idNumber (without hash) are made available to the Verifier \u001b[0m",  end="\n\n")
        print("\u001b[35;1m(i) The Verifier calculates and compares the values of the \u001b[0m",'\n\n' ,"    1. Decrypted message and", '\n\n' ,"    2. Hash(idNumber)",'\n\n' ,"\u001b[35;1mIf these 2 values are same then its authenticated using Digital Signature \u001b[0m",  end="\n\n")
        concat_message = str(idNumber) 
        print("\u001b[35;1m(j) Hash of the message is calculated: \u001b[0m",  end="\n\n")
        verification_hash= hashlib.sha256(concat_message.encode('utf-8')).hexdigest()
        verification_hash = int(verification_hash,16)
        print("\u001b[33;1mHash(idNumber): \u001b[0m", verification_hash, end="\n\n")
        
        print("\u001b[35;1m(k) Decrypting the message(without Hash) using (digital_signature s)^(public key)mod n = (message_hash)^((private key)*(public key))mod n = (message_hash)^1 mod n = (message_hash): \u001b[0m", end='\n\n')
        decrypted_message = pow(s, public_key, n)
        print("\u001b[33;1mDecrypted Message: \u001b[0m", decrypted_message, end="\n\n")
        if decrypted_message == verification_hash:
            a=1

        if a==1:
            print("\u001b[32;1mVoter Authenticated\u001b[0m")
        self.p.poll_response(poll_,a)
    
pm = poll_machine()