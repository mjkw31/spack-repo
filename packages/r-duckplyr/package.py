# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDuckplyr(RPackage):
	"""A 'DuckDB'-Backed Version of 'dplyr'

	A drop-in replacement for 'dplyr', powered by 'DuckDB' for performance.
    Also defines a set of generics that provide a low-level
    implementer's interface for the high-level user interface of 'dplyr'.
	"""
	
	homepage = "https://duckdblabs.github.io/duckplyr/"
	cran = "duckplyr" 

	version("0.3.0", md5="30a91b79c358a6c2336770c4d6793dda")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-collections", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-duckdb@0.9.1.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs@0.6.3:", type=("build", "run"))
