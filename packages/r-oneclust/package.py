# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROneclust(RPackage):
	"""Maximum Homogeneity Clustering for Univariate Data

	Maximum homogeneity clustering algorithm for one-dimensional data
    described in W. D. Fisher (1958) <doi:10.1080/01621459.1958.10501479>
    via dynamic programming.
	"""
	
	homepage = "https://nanx.me/oneclust/"
	cran = "oneclust" 

	version("0.2.3", md5="41e699ee7f43bcbdf903f62037e1b4a6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
