# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaspar2014(RPackage):
	"""Data package for JASPAR

	Data package for JASPAR 2014. To search this databases, please use the package TFBSTools.
	"""
	
	homepage = "http://jaspar.genereg.net/"
	bioc = "JASPAR2014" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/JASPAR2014_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/JASPAR2014/JASPAR2014_1.38.0.tar.gz"]

	version("1.38.0", md5="6ef536411db46944f6d5b9a23ee13be6", url="https://www.bioconductor.org/packages/release/data/experiment/src/contrib/JASPAR2014_1.38.0.tar.gz")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-biostrings@2.29.19:", type=("build", "run"))

	# experiment