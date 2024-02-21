# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigrquery(RPackage):
	"""An Interface to Google's 'BigQuery' 'API'

	Easily talk to Google's 'BigQuery' database from R.
	"""
	
	homepage = "https://bigrquery.r-dbi.org"
	cran = "bigrquery" 

	version("1.5.0", md5="3e011bbd218921b16f42c1147d66b118")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-brio", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-clock", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-gargle@1.4:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-prettyunits", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-rapidjsonr", type=("build", "run"))
