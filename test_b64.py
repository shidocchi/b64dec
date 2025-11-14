# coding:utf-8

import unittest
import binascii
import b64

class B64Test(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_01d(self):
    """raise exception if not enough 1byte"""
    with self.assertRaises(binascii.Error):
      b64.b64dec('A')

  def test_02d(self):
    """decode 2digit into 1byte"""
    self.assertEqual('00', b64.b64dec('AA'))
    self.assertEqual('01', b64.b64dec('AQ'))
    self.assertEqual('fe', b64.b64dec('_g'))
    self.assertEqual('ff', b64.b64dec('_w'))

  def test_03d(self):
    """decode 3digit into 2byte"""
    self.assertEqual('0000', b64.b64dec('AAA'))
    self.assertEqual('0001', b64.b64dec('AAE'))
    self.assertEqual('fffe', b64.b64dec('__4'))
    self.assertEqual('ffff', b64.b64dec('__8'))

  def test_04d(self):
    """decode 4digit into 3byte"""
    self.assertEqual('000000', b64.b64dec('AAAA'))
    self.assertEqual('000001', b64.b64dec('AAAB'))
    self.assertEqual('fffffe', b64.b64dec('___-'))
    self.assertEqual('ffffff', b64.b64dec('____'))

  def test_05d(self):
    """raise exception if not enough 1byte"""
    with self.assertRaises(binascii.Error):
      b64.b64dec('AAAAA')

  def test_06d(self):
    """decode 6digit into 4byte"""
    self.assertEqual('00000000', b64.b64dec('AAAAAA'))
    self.assertEqual('00000001', b64.b64dec('AAAAAQ'))
    self.assertEqual('fffffffe', b64.b64dec('_____g'))
    self.assertEqual('ffffffff', b64.b64dec('_____w'))

  def test_11d(self):
    """decode 11digit into 8byte"""
    self.assertEqual('0000000000000000', b64.b64dec('AAAAAAAAAAA'))
    self.assertEqual('0000000000000001', b64.b64dec('AAAAAAAAAAE'))
    self.assertEqual('fffffffffffffffe', b64.b64dec('__________4'))
    self.assertEqual('ffffffffffffffff', b64.b64dec('__________8'))

  def test_1b(self):
    """encode 1byte into 2digit"""
    self.assertEqual('AA', b64.b64enc('00'))
    self.assertEqual('AQ', b64.b64enc('01'))
    self.assertEqual('_g', b64.b64enc('fe'))
    self.assertEqual('_w', b64.b64enc('ff'))

  def test_2b(self):
    """encode 2byte into 3digit"""
    self.assertEqual('AAA', b64.b64enc('0000'))
    self.assertEqual('AAE', b64.b64enc('0001'))
    self.assertEqual('__4', b64.b64enc('fffe'))
    self.assertEqual('__8', b64.b64enc('ffff'))

  def test_3b(self):
    """encode 3byte into 4digit"""
    self.assertEqual('AAAA', b64.b64enc('000000'))
    self.assertEqual('AAAB', b64.b64enc('000001'))
    self.assertEqual('___-', b64.b64enc('fffffe'))
    self.assertEqual('____', b64.b64enc('ffffff'))

  def test_4b(self):
    """encode 4byte into 6digit"""
    self.assertEqual('AAAAAA', b64.b64enc('00000000'))
    self.assertEqual('AAAAAQ', b64.b64enc('00000001'))
    self.assertEqual('_____g', b64.b64enc('fffffffe'))
    self.assertEqual('_____w', b64.b64enc('ffffffff'))

  def test_8b(self):
    """encode 8byte into 11digit"""
    self.assertEqual('AAAAAAAAAAA', b64.b64enc('0000000000000000'))
    self.assertEqual('AAAAAAAAAAE', b64.b64enc('0000000000000001'))
    self.assertEqual('__________4', b64.b64enc('fffffffffffffffe'))
    self.assertEqual('__________8', b64.b64enc('ffffffffffffffff'))

if __name__ == "__main__":
    unittest.main()
