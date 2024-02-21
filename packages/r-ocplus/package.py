# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcplus(RPackage):
	"""Operating characteristics plus sample size and local fdr for microarray experiments

	This package allows to characterize the operating characteristics of a microarray experiment, i.e. the trade-off between false discovery rate and the power to detect truly regulated genes. The package includes tools both for planned experiments (for sample size assessment) and for already collected data (identification of differentially expressed genes).
	"""
	
	bioc = "OCplus" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/OCplus_1.76.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/OCplus/OCplus_1.76.0.tar.gz"]

	version("1.76.0", md5="8093ec3c635bc4ba57d27f42c6c85c48")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-multtest@1.7.3:", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
