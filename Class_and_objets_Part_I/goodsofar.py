class PowerballGame:
    
    
    def __init__(self, winningTicket = []):
        
        """Construct a PowerballGame object
        :param winingTicket: a list of six integer winning numbers ( 5 white winning balls and 1 red winning ball)
        :type winningTicket: list of integers
        :param numbers: a list of six integers numbers in a ticket
        :type numbers: list of integers
        :rtype: None
        """
        
        self._winningTicket = winningTicket
        
        
    # Getter
    def get_winningTicket(self):
        """ Returns  the list of numbers of the winning ticket in a PowerballGame object.
            :returns: the list of numbers of the winning ticket.
            :rtype: list of integers
        """
        return self._winningTicket


    # Setters

    def set_winningTicket(self, winningTicket):
        """ Updates the list of numbers of the winning ticket  in a PoweballGame object.
            :param numbers: new values in the list of numbers in the winning ticket.
            :type numbers: list of integers
            :rtype: None
        """
        self._winningTicket = winningTicket
    
    
    
    '''
    def count_white_balls(self, other):
        """ Count the white balls in the ticket object.
            :returns: the count the white balls in ticket object.
            :rtype: int
        """ 
        
        counterWhite = 0
        
        for n in self._winningTicket[:-1]:
            if n in other._winningTicket:
                counterWhite +=1
        return counterWhite
        
    def count_red_balls(self,other):
        """ Count the red balls in the ticket object.
            :returns: the count the red balls in ticket object.
            :rtype: int
        """   
        counterRed = 0
    
        if self._winningTicket[-1] == other._winningTicket[-1]:
            counterRed = 1
        return counterRed
    '''
        
    def find_prizes(self):
        """ Calculates the prize obtained for a ticket object.
            :returns: the prize obtained for a ticket object.
            :rtype: int
        """
        # Enforces that all derived classes must override this method.
        raise NotImplementedError

    


class Tickets(PowerballGame):
    def __init__(self, ticket = [], winningTicket = []):
        """Construct a ticket object
        :param ticket: an list of six integer numbers
        :type ticket: list of integers
        :rtype: None
        """
        PowerballGame.__init__(self, winningTicket)
        self._ticket = ticket
       
    # Getter
    def get_ticket(self):
        """ Returns  the list of numbers of a ticket object.
            :returns: the list of numbers of a ticket object.
            :rtype: list of integers
        """
        return self._ticket 

    # Setters

    def set_ticket(self, ticket):
        """ Updates the list of numbers of a ticket object.
            :param numbers: new values in the list of numbers in a ticket object
            :type numbers: list of integers
            :rtype: None
        """
        self._ticket = ticket
        
    #Method
    def count_white_balls(self):
        """ Count the white balls in the ticket object.
            :returns: the count the white balls in ticket object.
            :rtype: int
        """ 
        
        counterWhite = 0
        
        for n in self.get_ticket()[:-1]:
            if n in self.get_winningTicket():
                counterWhite +=1
        return counterWhite
        
    def count_red_balls(self):
        """ Count the red balls in the ticket object.
            :returns: the count the red balls in ticket object.
            :rtype: int
        """   
        counterRed = 0
    
        if self.get_winningTicket()[-1] == self.get_ticket()[-1]:
            counterRed = 1
        return counterRed
    
    def find_prizes(self):
        """ Calculates the prize obtained for a ticket object.
            :returns: the prize obtained for a ticket object.
            :rtype: int
        """
        # Enforces that all derived classes must override this method.
        grand_prize = ''
        
        counterWhite = self.count_white_balls()
        counterRed = self.count_red_balls()
        
        
        
        if counterWhite == 5 and counterRed == 1:
            prize = grand_prize
        if counterWhite == 5 and counterRed == 0:
            prize = 1000000
        if counterWhite == 4 and counterRed == 1:
            prize = 50000
        if counterWhite == 4 and counterRed == 0:
            prize = 100
        if counterWhite == 3 and counterRed == 1:
            prize = 100
        if counterWhite == 2 and counterRed == 1:
            prize = 7
        if counterWhite == 1 and counterRed == 1:
            prize = 4
        if counterWhite == 0 and counterRed == 1:
            prize = 4
        return prize
    

numbers = [22,1,62,3,38,11] 
winningTicket1 = [62,38,11,22,3,11]
t = Tickets(numbers, winningTicket1)
print(t.find_prizes())
