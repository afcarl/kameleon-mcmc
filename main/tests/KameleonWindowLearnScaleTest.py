"""
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

Written (W) 2013 Heiko Strathmann
Written (W) 2013 Dino Sejdinovic
"""

from main.distribution.Banana import Banana
from main.distribution.Flower import Flower
from main.kernel.GaussianKernel import GaussianKernel
from main.mcmc.MCMCChain import MCMCChain
from main.mcmc.MCMCParams import MCMCParams
from main.mcmc.output.PlottingOutput import PlottingOutput
from main.mcmc.output.StatisticsOutput import StatisticsOutput
from main.mcmc.samplers.Kameleon import Kameleon
from main.mcmc.samplers.KameleonWindowLearnScale import \
    KameleonWindowLearnScale
from main.mcmc.samplers.StandardMetropolis import StandardMetropolis
from main.tools.Visualise import Visualise
from matplotlib.pyplot import show
from numpy.core.numeric import zeros, inf
from numpy.lib.twodim_base import eye
import cProfile
import pstats


def main():
    distribution = Banana(dimension=2, bananicity=0.1, V=100.0)
    distribution = Flower(amplitude=6, frequency=6, variance=1, radius=10, dimension=8)
#    Visualise.visualise_distribution(distribution, Z)
#    show()
#    
    sigma = 5
    print "using sigma", sigma
    kernel = GaussianKernel(sigma=sigma)
    
    mcmc_sampler = KameleonWindowLearnScale(distribution, kernel, stop_adapt=inf)
    
    start = zeros(distribution.dimension)
    mcmc_params = MCMCParams(start=start, num_iterations=30000)
    chain = MCMCChain(mcmc_sampler, mcmc_params)
    
#    chain.append_mcmc_output(PlottingOutput(distribution, plot_from=10000))
    chain.append_mcmc_output(StatisticsOutput(plot_times=False))
    chain.run()
    
    print distribution.emp_quantiles(chain.samples[10000:])
    
#    Visualise.visualise_distribution(distribution, chain.samples)

#cProfile.run("main()", "profile.tmp")
#p = pstats.Stats("profile.tmp")
#p.sort_stats("cumulative").print_stats(10)
main()