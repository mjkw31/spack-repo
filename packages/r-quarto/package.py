# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuarto(RPackage):
	"""R Interface to 'Quarto' Markdown Publishing System

	Convert R Markdown documents and 'Jupyter' notebooks to a variety of
  output formats using 'Quarto'.
	"""
	
	homepage = "https://github.com/quarto-dev/quarto-r"
	cran = "quarto"

	version("1.3", md5="ab1e1e191b431dbd849d5c02fceed982")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-rsconnect@0.8.26:", type=("build", "run"))
	depends_on("quarto-cli", type=("build", "link", "run"))
