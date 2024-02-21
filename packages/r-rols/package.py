# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRols(RPackage):
	"""An R interface to the Ontology Lookup Service

	The rols package is an interface to the Ontology Lookup Service (OLS) to access and query hundred of ontolgies directly from R.
	"""
	
	homepage = "http://lgatto.github.io/rols/"
	bioc = "rols" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rols_2.30.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rols/rols_2.30.1.tar.gz"]

	version("2.30.1", md5="dae024b25d99cb24428d289e1b629f36")

	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics@0.23.1:", type=("build", "run"))
