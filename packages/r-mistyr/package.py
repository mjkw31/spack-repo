# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMistyr(RPackage):
	"""Multiview Intercellular SpaTial modeling framework

	mistyR is an implementation of the Multiview Intercellular SpaTialmodeling framework (MISTy). MISTy is an explainable machine learning framework for knowledge extraction and analysis of single-cell, highly multiplexed, spatially resolved data. MISTy facilitates an in-depth understanding of marker interactions by profiling the intra- and intercellular relationships. MISTy is a flexible framework able to process a custom number of views. Each of these views can describe a different spatial context, i.e., define a relationship among the observed expressions of the markers, such as intracellular regulation or paracrine regulation, but also, the views can also capture cell-type specific relationships, capture relations between functional footprints or focus on relations between different anatomical regions. Each MISTy view is considered as a potential source of variability in the measured marker expressions. Each MISTy view is then analyzed for its contribution to the total expression of each marker and is explained in terms of the interactions with other measurements that led to the observed contribution.
	"""
	
	homepage = "https://saezlab.github.io/mistyR/"
	bioc = "mistyR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/mistyR_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/mistyR/mistyR_1.10.0.tar.gz"]

	version("1.10.0", md5="f21483e1d8c9575d0c27a9fa544cfb3c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-distances", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-filelock", type=("build", "run"))
	depends_on("r-furrr@0.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-readr@2:", type=("build", "run"))
	depends_on("r-ridge", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
