# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpork(RPackage):
	"""Generalized Label Formatting

	The 'spork' syntax describes
 label formatting concisely, supporting
 mixed nesting of subscripts and superscripts
 to arbitrary depth. It intends to be easy
 to read and write in plain text, and easy
 to convert to equivalent presentations
 in 'plotmath', 'latex', and 'html'.  Greek symbols
 and a multiplication symbol are explicitly
 supported. See ?as_spork and ?as_previews.
	"""
	
	cran = "spork" 

	version("0.2.3", md5="8e5c061dab695cc0a7efd9fc64a76cce")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-latexpdf", type=("build", "run"))
