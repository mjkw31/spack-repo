# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeclear(RPackage):
	"""Correction of batch effects in DNA methylation data

	Provides functions to detect and correct for batch effects in DNA methylation data. The core function is based on latent factor models and can also be used to predict missing values in any other matrix containing real numbers.
	"""
	
	homepage = "https://github.com/uds-helms/BEclear"
	bioc = "BEclear"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BEclear_2.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BEclear/BEclear_2.18.0.tar.gz"]

	version("2.18.0", md5="bd34703e5a35dfc888f0029395df2c80")

	depends_on("r-biocparallel@1.14.2:", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dixontest", type=("build", "run"))
	depends_on("r-ids", type=("build", "run"))
