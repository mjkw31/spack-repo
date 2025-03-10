# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReconsi(RPackage):
	"""Resampling Collapsed Null Distributions for Simultaneous Inference

	Improves simultaneous inference under dependence of tests by estimating a collapsed null distribution through resampling. Accounting for the dependence between tests increases the power while reducing the variability of the false discovery proportion. This dependence is common in genomics applications, e.g. when combining flow cytometry measurements with microbiome sequence counts.
	"""
	
	bioc = "reconsi" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/reconsi_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/reconsi/reconsi_1.14.0.tar.gz"]

	version("1.14.0", md5="884019da85885289094a2aed95d18314")

	depends_on("r-phyloseq", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
