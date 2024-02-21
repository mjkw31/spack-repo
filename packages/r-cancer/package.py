# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCancer(RPackage):
	"""A Graphical User Interface for accessing and modeling the Cancer Genomics Data of MSKCC

	The package is user friendly interface based on the cgdsr and other modeling packages to explore, compare, and analyse all available Cancer Data (Clinical data, Gene Mutation, Gene Methylation, Gene Expression, Protein Phosphorylation, Copy Number Alteration) hosted by the Computational Biology Center at Memorial-Sloan-Kettering Cancer Center (MSKCC).
	"""
	
	bioc = "canceR"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/canceR_1.36.2.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/canceR/canceR_1.36.2.tar.gz"]

	version("1.36.2", md5="7d3c7532e79982ee5db6e3aa3788381e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cbioportaldata", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-genetclassifier", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-phenotest", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-r-oo", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
	depends_on("tktable", type=("build", "link", "run"))
