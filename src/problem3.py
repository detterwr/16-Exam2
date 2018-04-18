"""
Exam 2, problem 3.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Will Detterman.  April 2018.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


###############################################################################
# DONE: 2.
#   In this problem, you will go through the methods of the  Person  class
#   that is defined below, one by one, in the order that they appear.
#   For each method:
#      (a) Read the method's doc-string (i.e., specification in double-quotes).
#            If you do not understand WHAT the method is to do,
#            ask your instructor to clarify it.
#      (b) Implement the method.
#      (c) Write whatever code you want in  main  to test your code.
#            We wrote SOME testing code in  main  just to get you started.
#
###############################################################################

def main():
    """ Tests the  Person  class. """
    # -------------------------------------------------------------------------
    # Here is some simple code for testing a small part of the  Person  class:
    # -------------------------------------------------------------------------

    # Test of the Person class
    print('testing class: should return 3')
    p = Person(3)
    print(p.age)



    # Test get_age:
    print('testing get_age: should return 9')
    p1 = Person(9)
    print(p1.get_age())  # Should print 9

    print('testing celebrate_birthday: ')
    p1.celebrate_birthday()

    print('testing celebrate_birthdays: age should be 13')

    p1.celebrate_birthdays(3)
    print(p1.get_age())


    print('testing older_person: age should be 26')

    print(p1.older_person().age)

    # -------------------------------------------------------------------------
    # WRITE MORE CODE HERE AS NEEDED to TEST the code that you write
    #   in the  Person  class.  You are graded only on your implementation of
    #   the  Person  class, NOT on the quality or quantity of these tests
    #   that you write here. So KEEP IT SIMPLE here in main.
    # -------------------------------------------------------------------------


class Person(object):
    def __init__(self, age):
        """
        What comes in:  The Person's age.
        Side effects: Sets instance variables as needed by the other methods.
        """
        # DONE: Implement and test this method.

        self.age = age


    def get_age(self):
        """ Returns this Person's age. """
        # DONE: Implement and test this method.

        return self.age


    def celebrate_birthday(self):
        """
        Increments this Person's age.
        ALso prints 'Happy birthday!'.
        """
        # DONE: Implement and test this method.


        self.age = self.age + 1
        print('Happy birthday!')


    def celebrate_birthdays(self, n):
        """
        What comes in: A non-negative integer n.
        Side effects:  Calls the  celebrate_birthday  method  n  times.
        """
        # DONE: Implement and test this method.

        for k in range(n):
            self.celebrate_birthday()



    def older_person(self):
        """
        Returns a new Person whose age is twice this Person's age.
        """
        # DONE: Implement and test this method.


        return Person(self.age*2)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()