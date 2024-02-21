# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROntologyplot(RPackage):
	"""Visualising Sets of Ontological Terms

	Create R plots visualising ontological terms and the relationships between them with various graphical options - Greene et al. 2017 <doi:10.1093/bioinformatics/btw763>.
	"""
	
	cran = "ontologyPlot" 

	version("1.6", md5="41b0e12b18b17d69e43176af5c897af6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-paintmap", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
