# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWinch(RPackage):
	"""Portable Native and Joint Stack Traces

	Obtain the native stack trace and fuse it with R's
    stack trace for easier debugging of R packages with native code.
	"""
	
	homepage = "https://r-prof.github.io/winch/"
	cran = "winch" 

	version("0.1.0", md5="ae322afe751d5aa656dcd1cda16d53fb")

	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-procmaps@0.0.2:", type=("build", "run"))
