# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXpose4(RPackage):
	"""Diagnostics for Nonlinear Mixed-Effect Models

	A model building aid for nonlinear mixed-effects 
    (population) model analysis using NONMEM, facilitating data set 
    checkout, exploration and visualization, model diagnostics, candidate 
    covariate identification and model comparison. The methods are described 
    in Keizer et al. (2013) <doi:10.1038/psp.2013.24>, and Jonsson et al. (1999) 
    <doi:10.1016/s0169-2607(98)00067-4>.
	"""
	
	homepage = "https://uupharmacometrics.github.io/xpose4/"
	cran = "xpose4" 

	version("4.7.2", md5="7c6ea2c5a3778640e31009e5a7c2d6fe", url="https://cran.r-project.org/src/contrib/xpose4_4.7.2.tar.gz")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
