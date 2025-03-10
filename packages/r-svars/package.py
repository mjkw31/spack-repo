# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvars(RPackage):
	"""Data-Driven Identification of SVAR Models

	Implements data-driven identification methods for structural vector autoregressive (SVAR) models as described in Lange et al. (2021) <doi:10.18637/jss.v097.i05>. 
			 Based on an existing VAR model object (provided by e.g. VAR() from the 'vars' package), the structural 
			 impact matrix is obtained via data-driven identification techniques (i.e. changes in volatility (Rigobon, R. (2003) <doi:10.1162/003465303772815727>),  patterns of GARCH (Normadin, M., Phaneuf, L. (2004) <doi:10.1016/j.jmoneco.2003.11.002>),
			 independent component analysis (Matteson, D. S, Tsay, R. S., (2013) <doi:10.1080/01621459.2016.1150851>), least dependent innovations (Herwartz, H., Ploedt, M., (2016) <doi:10.1016/j.jimonfin.2015.11.001>), 
			 smooth transition in variances (Luetkepohl, H., Netsunajev, A. (2017) <doi:10.1016/j.jedc.2017.09.001>) or non-Gaussian maximum likelihood (Lanne, M., Meitz, M., Saikkonen, P. (2017) <doi:10.1016/j.jeconom.2016.06.002>)).
	"""
	
	cran = "svars"

	version("1.3.11", md5="8852be226665da8cdc261cfb9cae8425")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-vars@1.5.3:", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-steadyica", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
