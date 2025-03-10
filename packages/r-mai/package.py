# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMai(RPackage):
	"""Mechanism-Aware Imputation

	A two-step approach to imputing missing data in metabolomics. Step 1 uses a random forest classifier to classify missing values as either Missing Completely at Random/Missing At Random (MCAR/MAR) or Missing Not At Random (MNAR). MCAR/MAR are combined because it is often difficult to distinguish these two missing types in metabolomics data. Step 2 imputes the missing values based on the classified missing mechanisms, using the appropriate imputation algorithms. Imputation algorithms tested and available for MCAR/MAR include Bayesian Principal Component Analysis (BPCA), Multiple Imputation No-Skip K-Nearest Neighbors (Multi_nsKNN), and Random Forest. Imputation algorithms tested and available for MNAR include nsKNN and a single imputation approach for imputation of metabolites where left-censoring is present.
	"""
	
	homepage = "https://github.com/KechrisLab/MAI"
	bioc = "MAI" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MAI_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MAI/MAI_1.8.0.tar.gz"]

	version("1.8.0", md5="ac8dbd997d58657f8ed6b64f5cdee7a9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
