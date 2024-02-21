# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSasmap(RPackage):
	"""Static 'SAS' Code Analysis

	A static code analysis tool for 'SAS' scripts. It is designed to load, count, extract, remove, and summarise components of 'SAS' code.
	"""
	
	homepage = "https://github.com/MangoTheCat/sasMap"
	cran = "sasMap" 

	version("1.0.0", md5="e05fe56afa3ac4a24ed9a3bb66af0464")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
