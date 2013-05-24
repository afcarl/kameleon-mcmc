from main.distribution.Ring import Ring
from main.kernel.GaussianKernel import GaussianKernel
from main.mcmc.MCMCChain import MCMCChain
from main.mcmc.MCMCParams import MCMCParams
from main.mcmc.output.PlottingOutput import PlottingOutput
from main.mcmc.output.ProgressOutput import ProgressOutput
from main.mcmc.samplers.MCMCHammerWindow import MCMCHammerWindow
from main.tools.Visualise import Visualise
from numpy.ma.core import array
from main.mcmc.output.StatisticsOutput import StatisticsOutput

if __name__ == '__main__':
    distribution = Ring()
    
    sigma = GaussianKernel.get_sigma_median_heuristic(distribution.sample(1000).samples)
    print "using sigma", sigma
    kernel = GaussianKernel(sigma=sigma)
    
    mcmc_sampler = MCMCHammerWindow(distribution, kernel)
    
    start = array([-2, -2])
    mcmc_params = MCMCParams(start=start, num_iterations=10000)
    chain = MCMCChain(mcmc_sampler, mcmc_params)
    
    chain.append_mcmc_output(ProgressOutput())
    chain.append_mcmc_output(PlottingOutput(distribution, plot_from=2000))
    chain.append_mcmc_output(StatisticsOutput())
    chain.run()
    
    Visualise.visualise_distribution(distribution, chain.samples)