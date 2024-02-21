# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreesim(RPackage):
	"""Simulating Phylogenetic Trees

	Simulation methods for phylogenetic trees where (i) all tips are sampled at one time point or (ii) tips are sampled sequentially through time. (i) For sampling at one time point, simulations are performed under a constant rate birth-death process, conditioned on having a fixed number of final tips (sim.bd.taxa()), or a fixed age (sim.bd.age()), or a fixed age and number of tips (sim.bd.taxa.age()). When conditioning on the number of final tips, the method allows for shifts in rates and mass extinction events during the birth-death process (sim.rateshift.taxa()). The function sim.bd.age() (and sim.rateshift.taxa() without extinction) allow the speciation rate to change in a density-dependent way. The LTT plots of the simulations can be displayed using LTT.plot(), LTT.plot.gen() and LTT.average.root(). TreeSim further samples trees with n final tips from a set of trees generated by the common sampling algorithm stopping when a fixed number m>>n of tips is first reached (sim.gsa.taxa()). This latter method is appropriate for m-tip trees generated under a big class of models (details in the sim.gsa.taxa() man page). For incomplete phylogeny, the missing speciation events can be added through simulations (corsim()). (ii) sim.rateshifts.taxa() is generalized to sim.bdsky.stt() for serially sampled trees, where the trees are conditioned on either the number of sampled tips or the age. Furthermore, for a multitype-branching process with sequential sampling, trees on a fixed number of tips can be simulated using sim.bdtypes.stt.taxa(). This function further allows to simulate under epidemiological models with an exposed class. The function sim.genespeciestree() simulates coalescent gene trees within birth-death species trees, and sim.genetree() simulates coalescent gene trees.
	"""
	
	cran = "TreeSim" 

	version("2.4", md5="f2f433cadfac781a4a96ea1381f32a59")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
