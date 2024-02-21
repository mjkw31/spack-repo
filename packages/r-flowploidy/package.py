# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowploidy(RPackage):
	"""Analyze flow cytometer data to determine sample ploidy

	Determine sample ploidy via flow cytometry histogram analysis. Reads Flow Cytometry Standard (FCS) files via the flowCore bioconductor package, and provides functions for determining the DNA ploidy of samples based on internal standards.
	"""
	
	homepage = "https://github.com/plantarum/flowPloidy"
	bioc = "flowPloidy" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/flowPloidy_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/flowPloidy/flowPloidy_1.28.0.tar.gz"]

	version("1.28.0", md5="1020981a0f645d2dcbf1a38a3e42b7e0")

	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
