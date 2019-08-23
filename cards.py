# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:58:55 2017

@author: Dell1
v.0 creating a class Card which has attributes of real world entity Card viz Face,
Face_value(card_value),color,suit
"""

class Card:
    #defining the object card by instantiating face and suit
    def __init__(self,face,suit):
        self.face=face
        self.suit=suit
        
    @property 
    #property to get the card value based on face
    def card_values(self):
        if self.face.capitalize()=='Ace':
            card_value=1
            return card_value
        elif self.face.capitalize()=='Jack':
            card_value=11
            return card_value
        elif self.face.capitalize()=='Queen':
            card_value=12
            return card_value
        elif self.face.capitalize()=='King':
            card_value=13
            return card_value
        else:
            return(int(self.face))
    
    @property 
    #property to get the color of the cards based on suit
    def colors(self):
        if self.suit.capitalize() in ('Heart','Diamond'):
            color='Red'
            return color
        elif self.suit.capitalize() in ('Club','Spade'):
            color='Black'
            return color
    
    
    #Methods to compare the card object  (Operator overloading)   
    def __eq__(self,other):
        if isinstance(other,Card):
            return self.face==other.face and self.suit==other.suit
        elif isinstance(other,str):
            return str(self)==other
    
    def __lt__(self,other):
        if isinstance(other,Card):
            return self.card_values<other.card_values
        elif isinstance(other,str):
            value,face=other.split(':')
            return self.card_values<int(value) 
        
        
    # Representation of the class instance   
    def __repr__(self):
        return 'Card({},{})'.format(self.face,self.suit)
    
    #string representation of the Card object
    def __str__(self):
        if self.face in ('Ace','Jack','Queen','King'):
            return str(self.face[0].upper())+':'+str(self.suit[0].upper())
        else:
            return str(self.face)+':'+str(self.suit[0].upper())
    
  
def main():
    card1=Card('1','Spade')
    card2=Card('1','Spade')
    print(card1==card2)
    print(card1<card2)
    print (repr(card1))
    print (card1)
    print(card1.colors)
    
if __name__=='__main__':
    main()



        
       

        
    