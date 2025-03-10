# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmcfb(RPackage):
	"""Differentially Methylated Cytosines via a Bayesian Functional Approach

	DMCFB is a pipeline for identifying differentially methylated cytosines using a Bayesian functional regression model in bisulfite sequencing data. By using a functional regression data model, it tries to capture position-specific, group-specific and other covariates-specific methylation patterns as well as spatial correlation patterns and unknown underlying models of methylation data. It is robust and flexible with respect to the true underlying models and inclusion of any covariates, and the missing values are imputed using spatial correlation between positions and samples. A Bayesian approach is adopted for estimation and inference in the proposed method.
	"""
	
	bioc = "DMCFB" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DMCFB_1.16.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DMCFB/DMCFB_1.16.1.tar.gz"]

	version("1.16.1", md5="35caed88b548f9a3021d686498cd9d55")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-speedglm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-benchmarkme", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
