# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIseeindex(RPackage):
	"""iSEE extension for a landing page to a custom collection of data sets

	This package provides an interface to any collection of data sets within a single iSEE web-application. The main functionality of this package is to define a custom landing page allowing app maintainers to list a custom collection of data sets that users can selected from and directly load objects into an iSEE web-application.
	"""
	
	homepage = "https://github.com/iSEE/iSEEindex"
	bioc = "iSEEindex" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/iSEEindex_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/iSEEindex/iSEEindex_1.0.0.tar.gz"]

	version("1.0.0", md5="98a9141431a3206fd242b5b0b4056c41")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-isee", type=("build", "run"))
	depends_on("r-paws-storage", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
