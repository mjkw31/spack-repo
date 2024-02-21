# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeplogo(RPackage):
	"""Dependency Logo

	Plots dependency logos from a set of aligned input sequences.
	"""
	
	cran = "DepLogo" 

	version("1.2", md5="5ab5eb1472f7add686b15e7808f2b687")

