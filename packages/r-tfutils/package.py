# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfutils(RPackage):
	"""TFutils

	This package helps users to work with TF metadata from various sources. Significant catalogs of TFs and classifications thereof are made available. Tools for working with motif scans are also provided.
	"""
	
	bioc = "TFutils" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TFutils_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TFutils/TFutils_1.22.0.tar.gz"]

	version("1.22.0", md5="a2e83bbaafa0e47d7dbbd17385bd15fb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
