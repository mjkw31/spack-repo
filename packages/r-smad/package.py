# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmad(RPackage):
	"""Statistical Modelling of AP-MS Data (SMAD)

	Assigning probability scores to protein interactions captured in affinity purification mass spectrometry (AP-MS) expriments to infer protein-protein interactions. The output would facilitate non-specific background removal as contaminants are commonly found in AP-MS data.
	"""
	
	bioc = "SMAD" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SMAD_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SMAD/SMAD_1.18.0.tar.gz"]

	version("1.18.0", md5="65f0eba6ed0bf086797b95b2c9da6dd6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcppalgos", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
