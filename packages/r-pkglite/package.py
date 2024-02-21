# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkglite(RPackage):
	"""Compact Package Representations

	A tool, grammar, and standard to represent and exchange
    R package source code as text files. Converts one or more source
    packages to a text file and restores the package structures from the file.
	"""
	
	homepage = "https://merck.github.io/pkglite/"
	cran = "pkglite" 

	version("0.2.1", md5="7d62490287656ccc16354f4ab84a609b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
