# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBandits(RPackage):
	"""BANDITS: Bayesian ANalysis of DIfferenTial Splicing

	BANDITS is a Bayesian hierarchical model for detecting differential splicing of genes and transcripts, via differential transcript usage (DTU), between two or more conditions. The method uses a Bayesian hierarchical framework, which allows for sample specific proportions in a Dirichlet-Multinomial model, and samples the allocation of fragments to the transcripts. Parameters are inferred via Markov chain Monte Carlo (MCMC) techniques and a DTU test is performed via a multivariate Wald test on the posterior densities for the average relative abundance of transcripts.
	"""
	
	homepage = "https://github.com/SimoneTiberi/BANDITS"
	bioc = "BANDITS"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BANDITS_1.18.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BANDITS/BANDITS_1.18.1.tar.gz"]

	version("1.18.1", md5="2a65b9a4669d4075f5882047445491eb")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-drimseq", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
