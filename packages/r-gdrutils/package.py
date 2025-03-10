# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdrutils(RPackage):
	"""A package with helper functions for processing drug response data

	This package contains utility functions used throughout the gDR platform to fit data, manipulate data, and convert and validate data structures. This package also has the necessary default constants for gDR platform. Many of the functions are utilized by the gDRcore package.
	"""
	
	bioc = "gDRutils" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/gDRutils_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/gDRutils/gDRutils_1.0.0.tar.gz"]

	version("1.0.0", md5="fdf71802bbd5967b163447eda2fe37ef")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-bumpymatrix", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-jsonvalidate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
