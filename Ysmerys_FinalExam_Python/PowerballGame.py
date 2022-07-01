class PowerballGame:
    
    def __init__(self, winningNumbers, grand_prize):
        """Construct a PowerballGame object
        :param winingNumbers: a list of six integer numbers that represent the winning numbers ( 5 white balls and 1 red ball)
        :type winningNumbers: list of integers
        :param grand_prize: the value of the grand_prize
        :type grand_prize: int
        :rtype: None
        
        """
        self._winningNumbers = winningNumbers
        self._grand_prize = grand_prize
        
        
    # Getter
    def get_winningNumbers(self):
        """ Returns  the list of  winning numbers in a PowerballGame object.
            :returns: the list of winning numbers.
            :rtype: list of integers
            
        """
        return self._winningNumbers
    
    def get_grand_prize(self):
        """ Returns  the value of the grand prize for a PowerballGame object.
            :returns: the value of the grand prize.
            :rtype: int
            
        """
        return self._grand_prize


    # Setters

    def set_winningNumbers(self, winningNumbers):
        """ Updates the list of winning numbers of a PoweballGame object.
            :param winningNumbers: new values in the list of winning numbers.
            :type winningNumbers: list of integers
            :rtype: None
            
        """
        self._winningNumbers = winningNumbers
        
    def set_grand_prize(self, grand_prize):
        """ Updates the value of the grand prize in a PoweballGame object.
            :param grand_prize: new value of the grand_prize.
            :type numbers: int
            :rtype: None
            
        """
        self._grand_prize = grand_prize
    
    
    # Methods
    def count_white_balls(self):
        """ Counts the coincidence between the white ball numbers in the winning numbers and the selected white balls in a ticket-player.
            :returns: the count of white ball numbers.
            :rtype: int
            
        """ 
        # Enforces that all derived classes must override this method.
        raise NotImplementedError
        
    def count_red_balls(self):
        """ Counts the coincidence between the red ball number in the winning numbers and the selected red ball in a ticket-player.
            :returns: the count of red ball in the object.
            :rtype: int
            
        """   
        # Enforces that all derived classes must override this method.
        raise NotImplementedError
    
        
    def find_prizes(self):
        """ Calculates the prize obtained for a ticket in the Powerball Game.
            :returns: the prize obtained for a ticket.
            :rtype: int
            
        """
        # Enforces that all derived classes must override this method.
        raise NotImplementedError

    
