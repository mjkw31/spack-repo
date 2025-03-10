# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTenxplore(RPackage):
	"""ontological exploration of scRNA-seq of 1.3 million mouse neurons from 10x genomics

	Perform ontological exploration of scRNA-seq of 1.3 million mouse neurons from 10x genomics.
	"""
	
	bioc = "tenXplore" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/tenXplore_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/tenXplore/tenXplore_1.24.0.tar.gz"]

	version("1.24.0", md5="13e1778f8b644661a521bb832af6e7d6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-restfulse@0.99.12:", type=("build", "run"))
	depends_on("r-ontoproc@0.99.7:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
