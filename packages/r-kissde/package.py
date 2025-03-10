# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKissde(RPackage):
	"""Retrieves Condition-Specific Variants in RNA-Seq Data

	Retrieves condition-specific variants in RNA-seq data (SNVs, alternative-splicings, indels). It has been developed as a post-treatment of 'KisSplice' but can also be used with user's own data.
	"""
	
	bioc = "kissDE" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/kissDE_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/kissDE/kissDE_1.22.0.tar.gz"]

	version("1.22.0", md5="4965ff949376a98c35a73f0784501b0b")

	depends_on("r-aods3", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dss", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
