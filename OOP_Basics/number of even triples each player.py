"""To solve the given problem, we need to define custom exception classes and implement a method that compares the counts of even triples for two players. Based on the comparison, we will determine the winner or raise the appropriate exception.

Steps:
Define custom exception classes outwicket and otherwicket.
Implement the match method that counts the even triples for each player.
Based on the counts, either print the winner or raise the appropriate exception.
"""

class allout(Exception):
    message= 'ALL OUT'
    
class otherplayerout(Exception):
    message='Player 2 wins'
    

class Match:
    def count_triple_even(self,Player):
        count=0
        for i in range(len(Player)-2):
            if Player[i]%2 ==0 and Player[i+1]%2 ==0 and Player[i+2]%2==0:
                count+=1
        return count
            
        
    def match(self, p1, p2):
        self.p1 = self.count_triple_even(p1)
        self.p2 = self.count_triple_even(p2)
        if self.p1> self.p2:
            print('P1 wins')
        elif self.p1< self.p2:
            raise otherplayerout( )
        else:
            raise allout()
        

# Sample usage
p1 = [2, 2, 4, 6]
p2 = [2, 4, 6, 6]

d = Match()
try:
    d.match(p1, p2)
except Exception as e:
    print(e.message)