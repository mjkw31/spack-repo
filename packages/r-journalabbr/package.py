# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJournalabbr(RPackage):
	"""Journal Abbreviations for BibTeX Documents

	Since the reference management software (such as 'Zotero', 'Mendeley') exports Bib file journal abbreviation is not detailed enough, the 'journalabbr' package only abbreviates the journal field of Bib file, and then outputs a new Bib file for generating reference format with journal abbreviation on other software (such as 'texstudio'). The abbreviation table is from 'JabRef'. At the same time, 'Shiny' application is provided to generate 'thebibliography', a reference format that can be directly used for latex paper writing based on 'Rmd' files.
	"""
	
	homepage = "https://github.com/zoushucai/journalabbr"
	cran = "journalabbr" 

	version("0.4.0", md5="2addb12ded59788f5bc8a4288d375459")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tidytable", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
