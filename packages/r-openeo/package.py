# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpeneo(RPackage):
	"""Client Interface for 'openEO' Servers

	Access data and processing functionalities of 'openEO' compliant back-ends in R.
	"""
	
	homepage = "https://github.com/Open-EO/openeo-r-client"
	cran = "openeo" 

	version("1.3.0", md5="802e1db88831cddcd26f6b47281e58ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr2@0.2.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-irdisplay", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
