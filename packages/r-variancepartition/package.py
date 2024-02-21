# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariancepartition(RPackage):
	"""Quantify and interpret drivers of variation in multilevel gene expression experiments

	Quantify and interpret multiple sources of biological and technical variation in gene expression experiments. Uses a linear mixed model to quantify variation in gene expression attributable to individual, tissue, time point, or technical variables.  Includes dream differential expression analysis for repeated measures.
	"""
	
	homepage = "http://bioconductor.org/packages/variancePartition"
	bioc = "variancePartition" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/variancePartition_1.32.3.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/variancePartition/variancePartition_1.32.3.tar.gz"]

	version("1.32.3", md5="8a4ece91ac81a08e3f3671f4513caf72")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbkrtest@0.4.4:", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-matrix@1.4:", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-remacor@0.0.15:", type=("build", "run"))
	depends_on("r-fancova", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lme4@1.1.33:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
