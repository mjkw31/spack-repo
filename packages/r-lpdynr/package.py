# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpdynr(RPackage):
	"""Land Productivity Dynamics Indicator

	It uses 'phenological' and productivity-related variables derived from time series of vegetation 
    indexes, such as the Normalized Difference Vegetation Index, to assess ecosystem dynamics and change, which 
    eventually might drive to land degradation. The final result of the Land Productivity Dynamics indicator 
    is a categorical map with 5 classes of land productivity dynamics, ranging from declining to increasing 
    productivity. See <https://www.sciencedirect.com/science/article/pii/S1470160X21010517/> for a description of the methods used in 
    the package to calculate the indicator.
	"""
	
	homepage = "https://github.com/xavi-rp/LPDynR"
	cran = "LPDynR" 

	version("1.0.4", md5="f5551fd7dd6c895b5f919586e3563c7c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-virtualspecies", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
