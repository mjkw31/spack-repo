# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStationery(RPackage):
	"""Working Examples for Reproducible Research Documents

	Templates, guides, and scripts for
    writing documents in 'LaTeX' and 'R markdown' to produce
    guides, slides, and reports. Special care is taken to
    illustrate use of templates and customization opportunities.
    Challenges and opportunities of 'HTML' output from 'R markdown'
    receive special attention. Includes several vignettes
    to assist new users of literate programming.
	"""
	
	cran = "stationery" 

	version("1.0", md5="6cea5e1db500bd14291168544187470a")

	depends_on("r-kutils", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
