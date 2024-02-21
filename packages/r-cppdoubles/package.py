# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCppdoubles(RPackage):
	"""Fast Relative Comparisons of Floating Point Numbers in 'C++'

	Compare double-precision floating point vectors using
    relative differences. All equality operations are calculated using
    'cpp11'.
	"""
	
	cran = "cppdoubles" 

	version("0.1.1", md5="70ccf709dbdcdbd9cc990633193076ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
