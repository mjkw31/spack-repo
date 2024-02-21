# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrt(RPackage):
	"""Item Response Theory and Computerized Adaptive Testing Functions

	A collection of Item Response Theory (IRT) and Computerized 
     Adaptive Testing (CAT) functions that are used in psychometrics. 
	"""
	
	homepage = "https://github.com/egonulates/irt"
	cran = "irt" 

	version("0.2.7", md5="f3e90d1fde21ceb4d48de8d534fcd736")

	depends_on("r-rcpp", type=("build", "run"))
