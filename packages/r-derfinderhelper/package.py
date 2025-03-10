# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDerfinderhelper(RPackage):
	"""derfinder helper package

	Helper package for speeding up the derfinder package when using multiple cores. This package is particularly useful when using BiocParallel and it helps reduce the time spent loading the full derfinder package when running the F-statistics calculation in parallel.
	"""
	
	homepage = "https://github.com/leekgroup/derfinderHelper"
	bioc = "derfinderHelper" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/derfinderHelper_1.36.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/derfinderHelper/derfinderHelper_1.36.0.tar.gz"]

	version("1.36.0", md5="2544077112525d7f25f34270ed365423")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-iranges@1.99.27:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-s4vectors@0.2.2:", type=("build", "run"))
