# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaddr(RPackage):
	"""Statistical tests for detecting differential distributions based on the 2-Wasserstein distance

	The package offers statistical tests based on the 2-Wasserstein distance for detecting and characterizing differences between two distributions given in the form of samples. Functions for calculating the 2-Wasserstein distance and testing for differential distributions are provided, as well as a specifically tailored test for differential expression in single-cell RNA sequencing data.
	"""
	
	homepage = "https://github.com/goncalves-lab/waddR.git"
	bioc = "waddR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/waddR_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/waddR/waddR_1.16.0.tar.gz"]

	version("1.16.0", md5="97a692c918d531e3d872dc17141cd112")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-arm@1.10.1:", type=("build", "run"))
	depends_on("r-eva", type=("build", "run"))
	depends_on("r-biocfilecache@2.6:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
