# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultigraphr(RPackage):
	"""Probability Models and Statistical Analysis of Random
Multigraphs

	Methods and models for analysing multigraphs as introduced by Shafie (2015) <doi:10.21307/joss-2019-011>, including methods to study local and global properties <doi:10.1080/0022250X.2016.1219732> and goodness of fit tests.
	"""
	
	homepage = "https://github.com/termehs/multigraphr"
	cran = "multigraphr" 

	version("0.1.0", md5="f799ba7fe6f4a50d8ec07fc1e1578316")

	depends_on("r@3.2:", type=("build", "run"))
