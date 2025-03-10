# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScfa(RPackage):
	"""SCFA: Subtyping via Consensus Factor Analysis

	Subtyping via Consensus Factor Analysis (SCFA) can efficiently remove noisy signals from consistent molecular patterns in multi-omics data. SCFA first uses an autoencoder to select only important features and then repeatedly performs factor analysis to represent the data with different numbers of factors. Using these representations, it can reliably identify cancer subtypes and accurately predict risk scores of patients.
	"""
	
	homepage = "https://github.com/duct317/SCFA"
	bioc = "SCFA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SCFA_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SCFA/SCFA_1.12.0.tar.gz"]

	version("1.12.0", md5="c4e7d00ff20faff6a8a14eddde8e7a84")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-torch@0.3:", type=("build", "run"))
	depends_on("r-coro", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
