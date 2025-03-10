# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarnival(RPackage):
	"""A CAusal Reasoning tool for Network Identification (from gene expression data) using Integer VALue programming

	An upgraded causal reasoning tool from Melas et al in R with updated assignments of TFs' weights from PROGENy scores. Optimization parameters can be freely adjusted and multiple solutions can be obtained and aggregated.
	"""
	
	homepage = "https://github.com/saezlab/CARNIVAL"
	bioc = "CARNIVAL" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CARNIVAL_2.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CARNIVAL/CARNIVAL_2.12.0.tar.gz"]

	version("2.12.0", md5="c5457d5d859c16cbec56532338f64fb0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
