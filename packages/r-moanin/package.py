# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoanin(RPackage):
	"""An R Package for Time Course RNASeq Data Analysis

	Simple and efficient workflow for time-course gene expression data, built on publictly available open-source projects hosted on CRAN and bioconductor. moanin provides helper functions for all the steps required for analysing time-course data using functional data analysis: (1) functional modeling of the timecourse data; (2) differential expression analysis; (3) clustering; (4) downstream analysis.
	"""
	
	bioc = "moanin" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/moanin_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/moanin/moanin_1.10.0.tar.gz"]

	version("1.10.0", md5="74f0ff5d927d538a2b41cdc9c1ee9fd9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-mass@1:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-nmi", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
