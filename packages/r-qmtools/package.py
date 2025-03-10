# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQmtools(RPackage):
	"""Quantitative Metabolomics Data Processing Tools

	The qmtools (quantitative metabolomics tools) package provides basic tools for processing quantitative metabolomics data with the standard SummarizedExperiment class. This includes functions for imputation, normalization, feature filtering, feature clustering, dimension-reduction, and visualization to help users prepare data for statistical analysis. This package also offers a convenient way to compute empirical Bayes statistics for which metabolic features are different between two sets of study samples. Several functions in this package could also be used in other types of omics data.
	"""
	
	homepage = "https://github.com/HimesGroup/qmtools"
	bioc = "qmtools" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/qmtools_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/qmtools/qmtools_1.6.0.tar.gz"]

	version("1.6.0", md5="941d7cbf1dc8c2622fe97bda18a2bf49")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-vim", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
