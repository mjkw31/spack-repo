# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrayqualitymetrics(RPackage):
	"""Quality metrics report for microarray data sets

	This package generates microarray quality metrics reports for data in Bioconductor microarray data containers (ExpressionSet, NChannelSet, AffyBatch). One and two color array platforms are supported.
	"""
	
	bioc = "arrayQualityMetrics" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/arrayQualityMetrics_3.58.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/arrayQualityMetrics/arrayQualityMetrics_3.58.0.tar.gz"]

	version("3.58.0", md5="65128c55b6181bdadb73d256e399091e")

	depends_on("r-affy", type=("build", "run"))
	depends_on("r-affyplm@1.27.3:", type=("build", "run"))
	depends_on("r-beadarray", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-gridsvg@1.4.3:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-hwriter", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-setrng", type=("build", "run"))
	depends_on("r-vsn@3.23.3:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
