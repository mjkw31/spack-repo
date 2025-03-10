# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChronos(RPackage):
	"""CHRONOS: A time-varying method for microRNA-mediated sub-pathway enrichment analysis

	A package used for efficient unraveling of the inherent dynamic properties of pathways. MicroRNA-mediated subpathway topologies are extracted and evaluated by exploiting the temporal transition and the fold change activity of the linked genes/microRNAs.
	"""
	
	bioc = "CHRONOS"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CHRONOS_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CHRONOS/CHRONOS_1.30.0.tar.gz"]

	version("1.30.0", md5="7d2e5d9c89ea0163868d7b51bfd1c952")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk@1.7:", type=("build", "link", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
