# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbparser(RPackage):
	"""Drugs Databases Parser

	This tool is for parsing public drug databases such as 'DrugBank' XML database <https://go.drugbank.com/>.
    The parsed data are then returned in a proper 'R' object called 'dvobject'.
	"""
	
	homepage = "https://docs.ropensci.org/dbparser/"
	cran = "dbparser" 

	version("2.0.1", md5="d7dd3edbf5b698fcc963658bc5eba938")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
