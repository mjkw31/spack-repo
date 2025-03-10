# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDialignr(RPackage):
	"""Dynamic Programming Based Alignment of MS2 Chromatograms

	To obtain unbiased proteome coverage from a biological sample, mass-spectrometer is operated in Data Independent Acquisition (DIA) mode. Alignment of these DIA runs establishes consistency and less missing values in complete data-matrix. This package implements dynamic programming with affine gap penalty based approach for pair-wise alignment of analytes. A hybrid approach of global alignment (through MS2 features) and local alignment (with MS2 chromatograms) is implemented in this tool.
	"""
	
	bioc = "DIAlignR"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/DIAlignR_2.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/DIAlignR/DIAlignR_2.10.0.tar.gz"]

	version("2.10.0", md5="b67387fec7e8a9e5de5189fecd7077aa")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-zoo@1.8.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-mzr@2.18:", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rmsnumpress", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
