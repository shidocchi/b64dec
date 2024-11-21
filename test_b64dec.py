# coding:utf-8

import unittest
import binascii
import b64dec

class B64DecTest(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_01d(self):
    """raise exception if not enough 1byte"""
    with self.assertRaises(binascii.Error):
      b64dec.b64dec('A')

  def test_02d(self):
    """decode 2digit into 1byte"""
    self.assertEqual('00', b64dec.b64dec('AA'))
    self.assertEqual('01', b64dec.b64dec('AQ'))
    self.assertEqual('fe', b64dec.b64dec('_g'))
    self.assertEqual('ff', b64dec.b64dec('_w'))

  def test_03d(self):
    """decode 3digit into 2byte"""
    self.assertEqual('0000', b64dec.b64dec('AAA'))
    self.assertEqual('0001', b64dec.b64dec('AAE'))
    self.assertEqual('fffe', b64dec.b64dec('__4'))
    self.assertEqual('ffff', b64dec.b64dec('__8'))

  def test_04d(self):
    """decode 4digit into 3byte"""
    self.assertEqual('000000', b64dec.b64dec('AAAA'))
    self.assertEqual('000001', b64dec.b64dec('AAAB'))
    self.assertEqual('fffffe', b64dec.b64dec('___-'))
    self.assertEqual('ffffff', b64dec.b64dec('____'))

  def test_05d(self):
    """raise exception if not enough 1byte"""
    with self.assertRaises(binascii.Error):
      b64dec.b64dec('AAAAA')

  def test_06d(self):
    """decode 6digit into 4byte"""
    self.assertEqual('00000000', b64dec.b64dec('AAAAAA'))
    self.assertEqual('00000001', b64dec.b64dec('AAAAAQ'))
    self.assertEqual('fffffffe', b64dec.b64dec('_____g'))
    self.assertEqual('ffffffff', b64dec.b64dec('_____w'))

  def test_11d(self):
    """decode 11digit into 8byte"""
    self.assertEqual('0000000000000000', b64dec.b64dec('AAAAAAAAAAA'))
    self.assertEqual('0000000000000001', b64dec.b64dec('AAAAAAAAAAE'))
    self.assertEqual('fffffffffffffffe', b64dec.b64dec('__________4'))
    self.assertEqual('ffffffffffffffff', b64dec.b64dec('__________8'))

if __name__ == "__main__":
    unittest.main()
