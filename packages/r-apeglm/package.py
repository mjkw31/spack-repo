# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApeglm(RPackage):
	"""Approximate posterior estimation for GLM coefficients

	apeglm provides Bayesian shrinkage estimators for effect sizes for a variety of GLM models, using approximation of the posterior for individual coefficients.
	"""
	
	bioc = "apeglm" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/apeglm_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/apeglm/apeglm_1.24.0.tar.gz"]

	version("1.24.0", md5="0f8e64bdd8eec2566238fdc487afabb8")

	depends_on("r-emdbook", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
