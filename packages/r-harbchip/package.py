# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarbchip(RPackage):
	"""Experimental Data Package: harbChIP

	data from a yeast ChIP-chip experiment
	"""
	
	bioc = "harbChIP" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/harbChIP_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/harbChIP/harbChIP_1.40.0.tar.gz"]

	version("1.40.0", md5="f5948fc0f4c1ced0a43e85c1885f5d9e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))

	# experiment