# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwikipathways(RPackage):
	"""rWikiPathways - R client library for the WikiPathways API

	Use this package to interface with the WikiPathways API. It provides programmatic access to WikiPathways content in multiple data and image formats, including official monthly release files and convenient GMT read/write functions.
	"""
	
	homepage = "https://github.com/wikipathways/rwikipathways"
	bioc = "rWikiPathways" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rWikiPathways_1.22.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rWikiPathways/rWikiPathways_1.22.1.tar.gz"]

	version("1.22.1", md5="4a836092dcb14297a316efeb45de307d")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
