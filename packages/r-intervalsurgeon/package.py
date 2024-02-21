# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntervalsurgeon(RPackage):
	"""Operating on Integer-Bounded Intervals

	Manipulate integer-bounded intervals including finding overlaps, piling and merging.
	"""
	
	cran = "IntervalSurgeon" 

	version("1.2", md5="7537d4054ff99e20d4c3958e4dcc6b75")

	depends_on("r-rcpp", type=("build", "run"))
