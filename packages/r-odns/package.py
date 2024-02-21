# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdns(RPackage):
	"""Access Scottish Health and Social Care Open Data

	Allows potential users of Scottish Health and Social Care Open Data
    (<https://www.opendata.nhs.scot/>) to easily explore and extract the
    available data.
	"""
	
	homepage = "https://github.com/jrh-dev/odns"
	cran = "odns" 

	version("1.0.2", md5="ab43d1e0d08cd5820dd2d510f6865bc7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
