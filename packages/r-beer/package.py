# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeer(RPackage):
	"""Bayesian Enrichment Estimation in R

	BEER implements a Bayesian model for analyzing phage-immunoprecipitation sequencing (PhIP-seq) data. Given a PhIPData object, BEER returns posterior probabilities of enriched antibody responses, point estimates for the relative fold-change in comparison to negative control samples, and more. Additionally, BEER provides a convenient implementation for using edgeR to identify enriched antibody responses.
	"""
	
	homepage = "https://github.com/athchen/beer/"
	bioc = "beer"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/beer_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/beer/beer_1.6.0.tar.gz"]

	version("1.6.0", md5="c8e6192a3f9bd04b62ed564c8164ba00")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-phipdata@1.1.1:", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("jags@4.3.0:", type=("build", "link", "run"))
