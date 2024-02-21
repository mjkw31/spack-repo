# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBingadsr(RPackage):
	"""Get Bing Ads Data via the 'Windsor.ai' API

	Collect  your data on digital marketing campaigns from bing Ads using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "bingadsR" 

	version("0.1.0", md5="8dd742811e5c531fa8992455538884c1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
