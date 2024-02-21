# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMelt(RPackage):
	"""Multiple Empirical Likelihood Tests

	Performs multiple empirical likelihood tests for linear and
    generalized linear models. The package offers an easy-to-use interface
    and flexibility in specifying hypotheses and calibration methods,
    extending the framework to simultaneous inferences. The core
    computational routines are implemented using the 'Eigen' C++ library
    and 'RcppEigen' interface, with OpenMP for parallel computation.
    Details of the testing procedures are given in Kim, MacEachern, and
    Peruggia (2023) <doi:10.1080/10485252.2023.2206919>. This work was supported 
    by the U.S. National Science Foundation under Grants No. SES-1921523 and 
    DMS-2015552.
	"""
	
	homepage = "https://docs.ropensci.org/melt/"
	cran = "melt" 

	version("1.10.0", md5="3f707d847a823a286c2109177071f6be")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-dqrng", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
