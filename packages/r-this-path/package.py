# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThisPath(RPackage):
	"""Get Executing Script's Path

	Determine the path of the executing script. Compatible
        with a few popular GUIs: 'Rgui', 'RStudio', 'VSCode',
        'Jupyter', 'Emacs', and 'Rscript' (shell). Compatible with
        several functions and packages: 'source()', 'sys.source()',
        'debugSource()' in 'RStudio', 'compiler::loadcmp()',
        'box::use()', 'knitr::knit()', 'plumber::plumb()',
        'shiny::runApp()', 'package:targets', and
        'testthat::source_file()'.
	"""
	
	homepage = "https://github.com/ArcadeAntics/this.path"
	cran = "this.path" 

	version("2.3.1", md5="b01db2d5d8f66b4dbc559380c4780ccd")

