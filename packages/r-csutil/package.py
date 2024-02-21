# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsutil(RPackage):
	"""Common Base-R Problems Relating to Lists

	Utility functions that help with common base-R problems relating to lists.
    Lists in base-R are very flexible. This package provides functions to quickly and easily
    characterize types of lists. That is, to identify if all elements in a list
    are null, data.frames, lists, or fully named lists. Other functionality is provided
    for the handling of lists, such as the easy splitting of lists into equally sized
    groups, and the unnesting of data.frames within fully named lists.
	"""
	
	homepage = "https://www.csids.no/csutil/"
	cran = "csutil" 

	version("2023.4.25", md5="31efe86d68f380c4147c454379040553")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
