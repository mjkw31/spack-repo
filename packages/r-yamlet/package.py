# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYamlet(RPackage):
	"""Versatile Curation of Table Metadata

	A YAML-based
 mechanism for working with table metadata. Supports
 compact syntax for creating, modifying, viewing, exporting,
 importing, displaying, and plotting metadata coded as column 
 attributes. The 'yamlet' dialect is valid 'YAML' with
 defaults and conventions chosen to improve readability. 
 See ?yamlet, ?decorate, ?modify, ?io_csv, and ?ggplot.decorated.
	"""
	
	cran = "yamlet" 

	version("0.10.33", md5="469fcf636fa5c36d48eda1f06ad5bd64")

	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-csv@0.6.2:", type=("build", "run"))
	depends_on("r-encode", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-spork", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
