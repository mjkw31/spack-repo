# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicrexposome(RPackage):
	"""Exposome and omic data associatin and integration analysis

	omicRexposome systematizes the association evaluation between exposures and omic data, taking advantage of MultiDataSet for coordinated data management, rexposome for exposome data definition and limma for association testing. Also to perform data integration mixing exposome and omic data using multi co-inherent analysis (omicade4) and multi-canonical correlation analysis (PMA).
	"""
	
	bioc = "omicRexposome" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/omicRexposome_1.24.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/omicRexposome/omicRexposome_1.24.2.tar.gz"]

	version("1.24.2", md5="3b7a896124164c0dd282c91c79d2db00")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rexposome", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-pma", type=("build", "run"))
	depends_on("r-omicade4", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-multidataset", type=("build", "run"))
	depends_on("r-smartsva", type=("build", "run"))
	depends_on("r-isva", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
