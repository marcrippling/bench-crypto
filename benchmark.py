
from __future__ import division, print_function, absolute_import, unicode_literals
import inspect
import time
import types

import random
import os

from cryptography.hazmat.backends import default_backend
import cryptography.hazmat.primitives.asymmetric.rsa
import cryptography.hazmat.primitives.asymmetric.ec
import cryptography.hazmat.primitives.asymmetric.padding


backend = default_backend()


def generateNBitString(bits):
	  #return Crypto.Util.number.long_to_bytes(generateNBitNumber(bits))
	  return os.urandom(bits//8)


class Perftest(object):
	"""
	Benchmark the test() of childclasses.

	First a few dummy rounds are executed to make sure
	all dynamic initializations are done.
	Then a baseline is established by counting how
	many iterations are executed in 1/20 second.
	Then a 'full' test is run by measuring and executing
	for 1 full second.
	"""
	def __init__(self, description):
		self.description = description
	
	def countrounds(self, to):
		""" count how many iterations of self.test() can be run in the given time span <to> """
		ts = time.perf_counter()
		te = ts+to
		count = 0
		while time.perf_counter() < te:
			self.test()
			count += 1
		return count

	def run(self, counttime, fulltime):
		""" run the test """
		try:
			for _ in range(4):
				self.test()
			nrounds = int(self.countrounds(counttime)*(fulltime/counttime))
			ts = time.perf_counter()
			for _ in range(nrounds):
				self.test()
			te = time.perf_counter()
		except Exception as e:
			print(e)
			te, ts = 1, 0
			nrounds = 0

		print('%8d iter in %8.4f sec : %10.1f iter/sec:  %s' % (nrounds, te-ts, nrounds/(te-ts), self.description))


class TestCryptRsa(Perftest):
	""" test cryptography RSA """
	keycache = {}
	
	def __init__(self, modbits, msgbits):
		super(TestCryptRsa, self).__init__("cryptography.rsa:%d/%d" % (modbits, msgbits))
		if modbits not in self.keycache:
			self.keycache[modbits] = backend.generate_rsa_private_key(65537, modbits)
		self.privkey = self.keycache[modbits]
		self.pubkey = self.privkey.public_key()
		self.msg = generateNBitString(msgbits)

	def test(self):
		# self.pubkey.encrypt(self.msg, cryptography.hazmat.primitives.asymmetric.padding.PKCS1v15())
		self.privkey.sign(self.msg, cryptography.hazmat.primitives.asymmetric.padding.PKCS1v15(), cryptography.hazmat.primitives.hashes.SHA1())
		

def create_benchmark_list():
	tests = []
    for modbits in (1024,2048,4096):
        for msgbits in (2,256,512,1024):
            test = TestCryptRsa(modbits, msgbits)
			tests.append(test)
    return tests

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Crypto benchmark')
    # parser.add_argument('--modexp', action='store_true')
    parser.add_argument('--baselinetest', type=float, default=0.005, help='How long to make the initial algorithm measurement')
    parser.add_argument('--fulltest', type=float, default=0.1, help='How long to actually measure the algorithm')
    args = parser.parse_args()

    tests = create_benchmark_list()

    for test in tests:
        test.run(args.baselinetest, args.fulltest)


if __name__ == '__main__':
    main()