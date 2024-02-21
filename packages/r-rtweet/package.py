# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtweet(RPackage):
	"""Collecting Twitter Data

	An implementation of calls designed to collect and organize
    Twitter data via Twitter's REST and stream Application Program
    Interfaces (API), which can be found at the following URL:
    <https://developer.twitter.com/en/docs>.
	"""
	
	homepage = "https://docs.ropensci.org/rtweet/"
	cran = "rtweet" 

	version("1.2.1", md5="565bf6ad5213675e63ec4a68e64f2dc2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bit64@4.0.5:", type=("build", "run"))
	depends_on("r-curl@4.3.2:", type=("build", "run"))
	depends_on("r-httr@1.3:", type=("build", "run"))
	depends_on("r-httr2@0.2.2:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.22:", type=("build", "run"))
	depends_on("r-lifecycle@1:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-tibble@1.3.4:", type=("build", "run"))
	depends_on("r-withr@2.5:", type=("build", "run"))
