# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGa4ghclient(RPackage):
	"""A Bioconductor package for accessing GA4GH API data servers

	GA4GHclient provides an easy way to access public data servers through Global Alliance for Genomics and Health (GA4GH) genomics API. It provides low-level access to GA4GH API and translates response data into Bioconductor-based class objects.
	"""
	
	homepage = "https://github.com/labbcb/GA4GHclient"
	bioc = "GA4GHclient" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GA4GHclient_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GA4GHclient/GA4GHclient_1.26.0.tar.gz"]

	version("1.26.0", md5="d0e8b9a21eda6320d15642c12fcb8392")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
