# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:37:51 2017

@author: Dell1
"""

from deck import Deck
from cards import Card

class NotFreecell:
    
    def __init__(self):
        self.deck1=Deck(1,13,4)
        self.deck1.add_card()
        self.deck1.shuffle_card()
        # empty freecells
        self.freecells=[]
        # empty foundations
        self.foundation=[[]for cols in range(4)]
        self.cascades=[[]for cols in range(8)]
        # deal the cards
        for cards in range(52):
            self.cascades[cards % 8].append(self.deck1.deal_card())
            
 #representation of class instance
    def __repr__(self):
      return 'NotFreecell()'
  
#  String representation of the freecell object 
    def __str__(self):
   
      # make a blank board using lists
      row = ['  ' for i in range(8)]
      rows = [row[:] for j in range(10)]
      # fill in the free cells
      for cell_num, cell in enumerate(self.freecells):
         rows[0][cell_num] = str(cell)
      # fill in the foundations
      for cascade_num, cascade in enumerate(self.foundation):
         if cascade:
            rows[0][cascade_num + 4] = str(cascade[-1])
      # fill in the tableau cascades
      for stack_num, stack in enumerate(self.cascades):
         for card_num, card in enumerate(stack):
            rows[card_num + 2][stack_num] = str(card)
     
      # convert to string and return
      return '\n' + '\n'.join([' '.join(row) for row in rows])
    
    
    # Define Method to place a card from the playing area into freecell
    def move_to_freecell(self,card_txt):
        if len(self.freecells)==4:
            print('Cannot move the card to freecell')
        else:
            #Find the card in the tableau cascade:
            for stack_num,stack in enumerate(self.cascades):
                if stack and card_txt==stack[-1]:
                    break
            #Find whether the card is last card.If it is a blocked card then it cannot be moved
            if self.cascades[stack_num][-1]!=card_txt:
                print('Card {} is blocked and cannot make the move'.format(card_txt))
            else:
                card=self.cascades[stack_num].pop()
                self.freecells.append(card)
    
    """From the command text get the card and its position 
    Position of the card is defined  as (column_no,row_no) both col_no and row_no start from index value=0
    index value of the element --->row no. of cascade where the card is placed and iteration value--->column no. of the card."""
    def get_card_position(self,card_txt):
            card_position=(-2,-2)
            card=(0,'S')
            #checking the card in Freecells
            if card_txt in self.freecells:
                card_position=(-1,self.freecells.index(card_txt))
                card=self.freecells[card_position[1]]
            #checking the card in cascades
            for stack_num,stack in enumerate(self.cascades):
                if card_txt in stack:
                    card_position=(stack_num,stack.index(card_txt))
                    card=stack[card_position[1]]
            return card,card_position

#position(0)will give the cascade no. and position(1)will give index value of the element              
    def move_to_sidelane(self,origin,target):
        self.get_card_position(origin)
        original_card,original_card_position=self.get_card_position(origin)
        target_card,target_card_position=self.get_card_position(target)
        if target_card!=self.cascades[target_card_position[0]][-1] or original_card!=self.cascades[original_card_position[0]][-1]:
            print('Invalid Move!')
        elif original_card.colors==target_card.colors or target_card.card_values-original_card.card_values!=1:
            print('Ooops cannot make the placement!')
        else:
            for stack_num,stack in enumerate(self.cascades):
                if stack_num==original_card_position[0]:
                    self.cascades[stack_num].remove(original_card)
                if stack_num==target_card_position[0]:
                    self.cascades[stack_num].append(original_card)
        
            
                
 #Function to move a card to an empty lane:               
    def move_to_emptylane(self,origin,lane_no):
        self.get_card_position(origin)
        original_card,original_card_position=self.get_card_position(origin)
        if len(self.cascades[lane_no]):
            return  'Lane is not Empty'
        #check to find if the card is at the end position
        elif original_card!=self.cascades[original_card_position[0]][-1]:
            return 'Card is not at end posititon'
        else:
            for stack_num,stack in enumerate(self.cascades):
                if len(stack)==0 and lane_no==stack_num:
                   self.cascades[lane_no].append(original_card) 
                   self.cascades[original_card_position[0]].remove(original_card)

#Check to see whether the card is sorted or not    
    def is_sorted(self,f_card):
        if f_card.card_values==1:
            return True
        #Check to find whether it is sorted
        for pile in self.foundation:
            for element in pile:
                if f_card.suit==element.suit and f_card.card_values-element.card_values==1:
                    return True
                else:
                    return False
        
    def move_to_foundation(self,origin):
       original_card,original_card_position=self.get_card_position(origin)
       if self.is_sorted(original_card)==True:
           if original_card==self.cascades[original_card_position[0]][-1] and original_card.suit=='Diamond':
               self.cascades[original_card_position[0]].remove(original_card)
               self.foundation[0].append(original_card)
           elif original_card==self.cascades[original_card_position[0]][-1] and original_card.suit=='Spade':
               self.cascades[original_card_position[0]].remove(original_card)
               self.foundation[1].append(original_card)
           elif original_card==self.cascades[original_card_position[0]][-1] and original_card.suit=='Heart':
               self.cascades[original_card_position[0]].remove(original_card)
               self.foundation[2].append(original_card)
           elif original_card==self.cascades[original_card_position[0]][-1] and original_card.suit=='Club':
               self.cascades[original_card_position[0]].remove(original_card)
               self.foundation[3].append(original_card)
           else :
               print('Card is in the blocked state and cannot be placed.')
               
        
    #Game finishes if all the cards are placed in foundation stacks
    def game_over(self):
        return [len(stack) for stack in self.foundation]==[13,13,13,13] 
    
    """
   Five commands which are defined for the freecell game are as follows:
   1.Move to Foundation
   2.Move to Freecell
   3.Move to Sidelane card
   4.Move to Emptylane
   5.Quit command
   """
    
    def find_command(self,command):
        words=command.split()
        if words[0]=='Quit':
            quit()
        elif words[3]=='Foundation':
            self.move_to_foundation(words[1])
        elif words[3]=='Freecell':
            self.move_to_freecell(words[1])
        elif words[3]=='Sidelane':
            self.move_to_sidelane(words[1],words[3])
        elif words[3]=='Emptylane':
            self.move_to_emptylane(words[1],words[3])
        else:
            return'Invalid command!'
  
#Loop for playing the game
    def game_play(self):
        command=''
        while not self.game_over() and 'Quit' not in command:
            print(self)
            command=input('Enter your move: ')
            print(self.find_command(command))
        if self.game_over():
            print('You Won!')
        else:
            print('You Lose!')
  
        
def main():
   freecell=NotFreecell()
   freecell.game_play()
    
    
if __name__ == "__main__":
    option=input('Do you want to play freecell?')
    if option=='yes':
        main()
    else:
        quit()
        
