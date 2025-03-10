# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpivizrchart(RPackage):
	"""R interface to epiviz web components

	This package provides an API for interactive visualization of genomic data using epiviz web components. Objects in R/BioConductor can be used to generate interactive R markdown/notebook documents or can be visualized in the R Studio's default viewer.
	"""
	
	bioc = "epivizrChart" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/epivizrChart_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/epivizrChart/epivizrChart_1.24.0.tar.gz"]

	version("1.24.0", md5="076ebf7f9141cb71df0867f480ff960c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-epivizrdata@1.5.1:", type=("build", "run"))
	depends_on("r-epivizrserver", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
