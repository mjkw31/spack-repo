# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmrs(RPackage):
	"""Variable Selection in Finite Mixture of AFT Regression and FMR Models

	The package obtains parameter estimation, i.e., maximum likelihood estimators (MLE), via the Expectation-Maximization (EM) algorithm for the Finite Mixture of Regression (FMR) models with Normal distribution, and MLE for the Finite Mixture of Accelerated Failure Time Regression (FMAFTR) subject to right censoring with Log-Normal and Weibull distributions via the EM algorithm and the Newton-Raphson algorithm (for Weibull distribution). More importantly, the package obtains the maximum penalized likelihood (MPLE) for both FMR and FMAFTR models (collectively called FMRs). A component-wise tuning parameter selection based on a component-wise BIC is implemented in the package. Furthermore, this package provides Ridge Regression and Elastic Net.
	"""
	
	bioc = "fmrs" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/fmrs_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/fmrs/fmrs_1.12.0.tar.gz"]

	version("1.12.0", md5="ccf41504ab27d93464e555b363ef406a")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
