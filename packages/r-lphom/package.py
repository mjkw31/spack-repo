# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLphom(RPackage):
	"""Ecological Inference by Linear Programming under Homogeneity

	Provides a bunch of algorithms based on linear programming for estimating, 
    under the homogeneity hypothesis, RxC ecological contingency tables 
    (or vote transition matrices) using exclusively aggregate
    data (from voting units). References: 
    Romero, Pavía, Martín and Romero (2020) <doi:10.1080/02664763.2020.1804842>.
    Pavía and Romero (2021a) <doi:10.31124/advance.14716638.v1>.
    Pavía and Romero (2021b) Symmetry estimating R×C vote transfer matrices from aggregate data.
	"""
	
	cran = "lphom" 

	version("0.3.1-1", md5="2041ce1e914fb9f7f5cfa30080d13668")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
