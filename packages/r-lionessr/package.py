# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLionessr(RPackage):
	"""Modeling networks for individual samples using LIONESS

	LIONESS, or Linear Interpolation to Obtain Network Estimates for Single Samples, can be used to reconstruct single-sample networks (https://arxiv.org/abs/1505.06440). This code implements the LIONESS equation in the lioness function in R to reconstruct single-sample networks. The default network reconstruction method we use is based on Pearson correlation. However, lionessR can run on any network reconstruction algorithms that returns a complete, weighted adjacency matrix. lionessR works for both unipartite and bipartite networks.
	"""
	
	homepage = "https://github.com/mararie/lionessR"
	bioc = "lionessR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/lionessR_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/lionessR/lionessR_1.16.0.tar.gz"]

	version("1.16.0", md5="4301a7fed98cbe717433fa80791ad9a6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
