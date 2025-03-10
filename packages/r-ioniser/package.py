# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIoniser(RPackage):
	"""Quality Assessment Tools for Oxford Nanopore MinION data

	IONiseR provides tools for the quality assessment of Oxford Nanopore MinION data. It extracts summary statistics from a set of fast5 files and can be used either before or after base calling.  In addition to standard summaries of the read-types produced, it provides a number of plots for visualising metrics relative to experiment run time or spatially over the surface of a flowcell.
	"""
	
	bioc = "IONiseR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/IONiseR_2.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/IONiseR/IONiseR_2.26.0.tar.gz"]

	version("2.26.0", md5="10a3ed3f75ba8be8989b90d197096b40")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
