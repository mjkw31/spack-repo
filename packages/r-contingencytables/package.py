# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContingencytables(RPackage):
	"""Statistical Analysis of Contingency Tables

	Provides functions to perform statistical inference of data organized in contingency tables. This package is a companion to the "Statistical Analysis of Contingency Tables" book by Fagerland et al. <ISBN 9781466588172>.
	"""
	
	homepage = "https://contingencytables.com/"
	cran = "contingencytables" 

	version("2.2.1", md5="a37b04d55db29da4976e082ab5a7c88a")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
