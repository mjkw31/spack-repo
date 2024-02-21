# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAltdoc(RPackage):
	"""Use 'Docsify.js', 'Docute', or 'Mkdocs' to Generate a Package
Documentation

	Most developers use 'pkgdown' to create a website for their packages.
    Other documentation generators exist, such as 'Docute', 'Docsify.js', or 'Mkdocs'. 
    The aim of 'altdoc' is to provide helpers to create, populate, update, and 
    preview websites made with these tools.
	"""
	
	homepage = "https://github.com/etiennebacher/altdoc"
	cran = "altdoc" 

	version("0.2.2", md5="4918fcba4693c701a9f9b03dd4af9a64")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-servr", type=("build", "run"))
	depends_on("r-tinkr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
