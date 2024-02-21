# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMimager(RPackage):
	"""mimager: The Microarray Imager

	Easily visualize and inspect microarrays for spatial artifacts.
	"""
	
	homepage = "https://github.com/aaronwolen/mimager"
	bioc = "mimager" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/mimager_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/mimager/mimager_1.26.0.tar.gz"]

	version("1.26.0", md5="2a9eaf36345d24dc2d44a65c1f8640a0")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-affyplm", type=("build", "run"))
	depends_on("r-oligo", type=("build", "run"))
	depends_on("r-oligoclasses", type=("build", "run"))
