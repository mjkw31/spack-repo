# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDccmidas(RPackage):
	"""DCC Models with GARCH-MIDAS Specifications in the Univariate
Step

	Estimates a variety of Dynamic Conditional Correlation (DCC) models. More in detail, the 'dccmidas' package allows the estimation of the corrected DCC (cDCC) of Aielli (2013) <doi:10.1080/07350015.2013.771027>, the DCC-MIDAS of Colacito et al. (2011) <doi:10.1016/j.jeconom.2011.02.013>, the Asymmetric DCC of Cappiello et al. <doi:10.1093/jjfinec/nbl005>, and the Dynamic Equicorrelation (DECO) of Engle and Kelly (2012) <doi:10.1080/07350015.2011.652048>. 'dccmidas' offers the possibility of including standard GARCH <doi:10.1016/0304-4076(86)90063-1>, GARCH-MIDAS <doi:10.1162/REST_a_00300> and Double Asymmetric GARCH-MIDAS <doi:10.1016/j.econmod.2018.07.025> models in the univariate estimation. Finally, the package calculates also the var-cov matrix under two non-parametric models: the Moving Covariance and the RiskMetrics specifications.
	"""
	
	cran = "dccmidas" 

	version("0.1.0", md5="a52a455c98dcd242951b4fcb3c4abc09")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-maxlik@1.3.8:", type=("build", "run"))
	depends_on("r-rumidas@0.1.1:", type=("build", "run"))
	depends_on("r-rugarch@1.4.4:", type=("build", "run"))
	depends_on("r-roll@1.1.4:", type=("build", "run"))
	depends_on("r-xts@0.12:", type=("build", "run"))
	depends_on("r-tseries@0.10.47:", type=("build", "run"))
	depends_on("r-rdpack@1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-zoo@1.8.8:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
