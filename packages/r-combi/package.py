# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombi(RPackage):
	"""Compositional omics model based visual integration

	This explorative ordination method combines quasi-likelihood estimation, compositional regression models and latent variable models for integrative visualization of several omics datasets. Both unconstrained and constrained integration are available. The results are shown as interpretable, compositional multiplots.
	"""
	
	bioc = "combi" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/combi_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/combi/combi_1.14.0.tar.gz"]

	version("1.14.0", md5="6fe16559db40b31126eb543abf6819fa")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-matrix@1.6:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-cobs", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
