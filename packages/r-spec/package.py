# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpec(RPackage):
	"""A Data Specification Format and Interface

	Creates a data specification that describes the columns of a 
 table (data.frame). Provides methods to read, write, and update the 
 specification. Checks whether a table matches its specification. See
 specification.data.frame(),read.spec(), write.spec(), as.csv.spec(),
 respecify.character(), and %matches%.data.frame().
	"""
	
	cran = "spec" 

	version("0.1.7", md5="7734b17d599627e5fc482b5a73fb43ad")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-encode", type=("build", "run"))
	depends_on("r-csv", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
