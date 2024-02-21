# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpranalyze(RPackage):
	"""Statistical Analysis of MPRA data

	MPRAnalyze provides statistical framework for the analysis of data generated by Massively Parallel Reporter Assays (MPRAs), used to directly measure enhancer activity. MPRAnalyze can be used for quantification of enhancer activity, classification of active enhancers and comparative analyses of enhancer activity between conditions. MPRAnalyze construct a nested pair of generalized linear models (GLMs) to relate the DNA and RNA observations, easily adjustable to various experimental designs and conditions, and provides a set of rigorous statistical testig schemes.
	"""
	
	homepage = "https://github.com/YosefLab/MPRAnalyze"
	bioc = "MPRAnalyze" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MPRAnalyze_1.20.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MPRAnalyze/MPRAnalyze_1.20.0.tar.gz"]

	version("1.20.0", md5="63ae4121bc319692b51499a1b151dffc")

	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
