# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecurse(RPackage):
	"""Computes Revisitation Metrics for Trajectory Data

	Computes revisitation metrics for trajectory data, such as the number of revisitations for each location as well as the time spent for that visit and the time since the previous visit. Also includes functions to plot data.
	"""
	
	cran = "recurse" 

	version("1.2.0", md5="422e6f8570cca3943be4ab54d477472b")

	depends_on("r-rcpp", type=("build", "run"))
