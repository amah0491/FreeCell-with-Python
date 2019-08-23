# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:27:09 2017

@author: Dell1
Deck is made up of Cards.The class is initialized by giving start_value,end_value and no.of suits 
to be included in the game play.
"""
from cards import Card
import random
face_list=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suit_list=['Diamond','Club','Heart','Spade']

       
        

class Deck:
    
    def __init__(self,start_value,end_value,suit_number):
        self.start_value=start_value
        self.end_value=end_value
        self.suit_number=suit_number
        self.card_list=[]
        self.cards_played=[]
        self.card_draw=[]
    
    #creating deck of cards which is stored in card_list using Card class  
    def add_card(self):
        #Creating a generalized Deck:
        if self.suit_number!=4:
            for suit in range(self.suit_number):
                for face in range(self.start_value,self.end_value+1):
                    self.card_list.append(Card(face,suit))
        #Creating a deck which is to be used in freecell
        elif self.suit_number==4:
            for suit in suit_list:
                for face in face_list:
                    self.card_list.append(Card(face,suit))
       
                    
                    
    def draw_card(self,card):
        self.cards_played.remove(card)
        self.card_draw.append(card)
        
    def shuffle_card(self):
       random.shuffle(self.card_list)
       return self.card_list
       
            
    def deal_card(self):
        card=self.card_list.pop()
        self.cards_played.append(card)
        return card

              

        
#representation of Deck instance    
    def __repr__(self):
        return 'Deck({},{},{})'.format(self.start_value,self.end_value,self.suit_number)
    
    
    def __str__(self):
        return 'No. of Cards: {}\nCards in deck:\n{}'.format(len(self.card_list),self.card_list)
        
            
            
        
        
    
def main(): 
    deck1=Deck(1,13,4)
    #deck1.shuffle_card()
    deck1.add_card()
#    print(deck1.card_list)
    
    #print(deck1.shuffle_card())
#    deck1.deal_card()
    print(repr(deck1))
    print(deck1)
#    deck2=Deck(1,13,4)
#    deck2.add_card()
#    print(deck2)
##    
###    print(deck1)
##    
##    #print(str(deck1))
##    #print(deck1)
##    
if __name__ == "__main__":
    main()
    


        
   








