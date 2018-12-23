#!/usr/bin/env python3
# gInt - unit testing
#
# Kevin Wong
# kmw396 - 14240214
# Lab 09 - UnitTesting
# 12/03
#

import sys
import unittest

from gInt import gInt  # the class I wrote, that I wish to test

class gIntTest( unittest.TestCase ) :
    '''Tests for gInt class'''
	
    def setUp( self ) :
        '''Optional.  Run before for each test.'''
        self.u1 = gInt(2,4)
        self.u1copy = gInt(2,4)
        self.u2 = gInt(3,6)
        self.u2copy = gInt(3,6)
        self.p1 = gInt(5,6)
        self.n1 = gInt(-7,-8)
        self.n2 = gInt(-8,-9)
        self.n2copy = gInt(-8,-9)
    def tearDown( self ) :
        '''Optional.  Called after each test (if setUp didn't fail)'''
        pass
    
    def test_add( self ) :
        r = self.u1 + self.u2
        self.assertEqual( self.u1, self.u1copy, 'Left operand changed after addition' )
        self.assertEqual( self.u2, self.u2copy, 'Right operand changed after addition' )
        self.assertEqual( r, (gInt( 2 , 4) + gInt( 3 , 6)), 'Addition failed' )
        r = self.u1 + self.n2
        self.assertEqual( r, (gInt( 2 , 4) + gInt( -8 , -9)), 'Addition of positive + negative failed' )
        r = self.n1 + self.n2
        self.assertEqual( r, (gInt( -7 , -8) + gInt( -8 , -9)), 'Addition of negative + negative failed' )        
    
    def test_mult( self ):
        r = self.u1 * self.u2
        self.assertEqual( self.u1, self.u1copy, 'Left operand changed after multiplication' )
        self.assertEqual( self.u2, self.u2copy, 'Right operand changed after multiplication' )
        self.assertEqual( r, (gInt( 2 , 4) * gInt( 3 , 6)), 'Multiplication failed' )
        r = self.u1 * self.n2
        self.assertEqual( r, (gInt( 2 , 4) * gInt( -8 , -9)), 'Multiplication of positive + negative failed' )
        r = self.n1 * self.n2
        self.assertEqual( r, (gInt( -7 , -8) * gInt( -8 , -9)), 'Multiplication of negative + negative failed' )       
    def test_norm( self ):
        r = 20
        self.assertEqual( self.u1.norm(), self.u1copy.norm(), 'Left operand changed after Norm' )
        self.assertEqual( self.u2.norm(), self.u2copy.norm(), 'Right operand changed after Norm' )
        self.assertEqual( r, self.u1.norm(), 'Norm failed')
        r = 113
        self.assertEqual( r, self.n1.norm(), 'Norm of negative failed')

if __name__ == '__main__' :
	sys.argv.append( '-v' )
	unittest.main()

