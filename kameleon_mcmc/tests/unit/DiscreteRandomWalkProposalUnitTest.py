"""
Copyright (c) 2013-2014 Heiko Strathmann
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
 *
1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
 *
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies,
either expressed or implied, of the author.
"""

from numpy import zeros, ones, asarray
import numpy
from numpy.random import rand, randint
import unittest

from kameleon_mcmc.distribution.DiscreteRandomWalkProposal import DiscreteRandomWalkProposal
from kameleon_mcmc.distribution.Distribution import Sample


class DiscreteRandomWalkProposalUnitTest(unittest.TestCase):
    def test_contructor_wrong_mu_type_float(self):
        mu = 0
        spread = 1.
        self.assertRaises(TypeError, DiscreteRandomWalkProposal, mu, spread)
        
    def test_contructor_wrong_mu_type_none(self):
        mu = None
        spread = 1.
        self.assertRaises(TypeError, DiscreteRandomWalkProposal, mu, spread)

    def test_contructor_wrong_mu_dim_too_large(self):
        mu = zeros((1, 2), dtype=numpy.bool8)
        spread = 1.
        self.assertRaises(ValueError, DiscreteRandomWalkProposal, mu, spread)
        
    def test_contructor_wrong_mu_dimension_0(self):
        mu = zeros(0, dtype=numpy.bool8)
        spread = 1.
        self.assertRaises(ValueError, DiscreteRandomWalkProposal, mu, spread)
        
    def test_contructor_wrong_spread_type_int(self):
        mu = zeros(2, dtype=numpy.bool8)
        spread = 1
        self.assertRaises(TypeError, DiscreteRandomWalkProposal, mu, spread)
                          
    def test_contructor_wrong_spread_type_none(self):
        mu = zeros(2, dtype=numpy.bool8)
        spread = None
        self.assertRaises(TypeError, DiscreteRandomWalkProposal, mu, spread)
        
    def test_contructor_wrong_spread_range_0(self):
        mu = ones(2, dtype=numpy.bool8)
        spread = 0.
        self.assertRaises(ValueError, DiscreteRandomWalkProposal, mu, spread)
        
    def test_contructor_wrong_spread_range_1(self):
        mu = ones(2, dtype=numpy.bool8)
        spread = 1.
        self.assertRaises(ValueError, DiscreteRandomWalkProposal, mu, spread)
        
    def test_contructor_correct_mu(self):
        mu = ones(2, dtype=numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        self.assertTrue(mu is dist.mu)
        
    def test_contructor_correct_spread(self):
        mu = ones(2, dtype=numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        self.assertEqual(spread, dist.spread)
        
#     
    def test_sample_wrong_n_sameller_zero(self):
        mu = randint(0, 2, 10).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        self.assertRaises(ValueError, dist.sample, -1)
     
    def test_sample_wrong_n_type_none(self):
        mu = randint(0, 2, 10).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        self.assertRaises(TypeError, dist.sample, None)
          
    def test_sample_wrong_n_type_float(self):
        mu = randint(0, 2, 10).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        self.assertRaises(TypeError, dist.sample, float(1.))
          
    def test_sample_type(self):
        mu = randint(0, 2, 10).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        s = dist.sample(1)
        self.assertTrue(isinstance(s, Sample))
          
    def test_sample_samples_dtype(self):
        mu = randint(0, 2, 10).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        s = dist.sample(1)
        self.assertEqual(s.samples.dtype, numpy.bool8)
          
    def test_sample_dim(self):
        n = 3
        d = 2
        mu = randint(0, 2, d).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        s = dist.sample(n)
        self.assertEqual(s.samples.shape, (n, d))
        
    def test_sample_many_no_checks(self):
        num_runs = 1000
        for _ in range(num_runs):
            n = randint(1, 10)
            d = randint(1, 10)
            mu = randint(0, 2, d).astype(numpy.bool8)
            spread = rand()
            dist = DiscreteRandomWalkProposal(mu, spread)
            dist.sample(n)
#                 
    def test_log_pdf_wrong_type_none(self):
        d = 2
        mu = randint(0, 2, d).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        self.assertRaises(TypeError, dist.log_pdf, None)
         
    def test_log_pdf_wrong_type_float(self):
        d = 2
        mu = randint(0, 2, d).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        self.assertRaises(TypeError, dist.log_pdf, float(1.))
         
    def test_log_pdf_wrong_array_dimension_1(self):
        d = 2
        mu = randint(0, 2, d).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        self.assertRaises(TypeError, dist.log_pdf, zeros(1))
         
    def test_log_pdf_wrong_array_dimension_3(self):
        d = 2
        mu = randint(0, 2, d).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        self.assertRaises(TypeError, dist.log_pdf, zeros(3))
         
    def test_log_pdf_wrong_dimension(self):
        d = 2
        mu = randint(0, 2, d).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        self.assertRaises(ValueError, dist.log_pdf, zeros((1, 3)))
         
    def test_log_pdf_type(self):
        d = 2
        mu = randint(0, 2, d).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        self.assertEqual(type(dist.log_pdf(asarray([[1, 2]], dtype=numpy.bool8))), numpy.ndarray)
     
    def test_log_pdf_array_dimension(self):
        d = 2
        n = randint(1, 19)
        mu = randint(0, 2, d).astype(numpy.bool8)
        spread = .5
        dist = DiscreteRandomWalkProposal(mu, spread)
        X = randint(0, 2, (n, d)).astype(numpy.bool8)
        self.assertEqual(dist.log_pdf(X).shape, (n,))
         
if __name__ == "__main__":
    unittest.main()
