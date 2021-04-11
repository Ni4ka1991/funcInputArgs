#!/usr/bin/env python3

from os import system

# #### LOGIC #####################################

def inputInt( message ):
 i = int( input( f"{message}" ))
 return i


def inputFloat( message ):
 i = float( input( f"{message}" ))
 return i


def inputBoolean( message ):
 i = ( input( f"{message}" ))
 if( i == "True" or "true" or "1"):
  i = True
 elif( i == "False" or "false" or "0" ):
  i = False
 else:
     print( "Enter another value." )

 return i

# ##############################################



# ###### VIEW ##################################

system( "clear" )

# I
# float #######

f = inputFloat( "Enter the first float >>>   " )
j = inputFloat( "Enter the second float >>>  " )
print( f + j )
# #############

# II
# integer #####

m = inputInt( "Enter the first integer >>>  " )
n = inputInt( "Enter the second integer >>> " )
print( n + m )

# #############

# III
# boolean #####

b = inputBoolean( "Enter the first boolean b >>>   " )
print( b )
c = inputBoolean( "Enter the second boolean c >>>  " )
print( c )
print( "c + b =", c and b)

# ###################################################
