# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcwl(RPackage):
	"""An R interface to the Common Workflow Language

	The Common Workflow Language (CWL) is an open standard for development of data analysis workflows that is portable and scalable across different tools and working environments. Rcwl provides a simple way to wrap command line tools and build CWL data analysis pipelines programmatically within R. It increases the ease of usage, development, and maintenance of CWL pipelines.
	"""
	
	bioc = "Rcwl" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Rcwl_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Rcwl/Rcwl_1.18.0.tar.gz"]

	version("1.18.0", md5="f427ee3f7f5ba2458f8f97b694b48a85")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-batchtools", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
