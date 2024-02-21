# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPromise(RPackage):
	"""PRojection Onto the Most Interesting Statistical Evidence

	A general tool to identify genomic features with a specific biologically interesting pattern of associations with multiple endpoint variables as described in Pounds et. al. (2009) Bioinformatics 25: 2013-2019
	"""
	
	bioc = "PROMISE" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/PROMISE_1.54.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/PROMISE/PROMISE_1.54.0.tar.gz"]

	version("1.54.0", md5="ad7b8b2fcd0ba52ad47eb9ff23097a4e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
