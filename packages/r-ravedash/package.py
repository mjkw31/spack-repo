# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRavedash(RPackage):
	"""Dashboard System for Reproducible Visualization of 'iEEG'

	Dashboard system to display the analysis results produced by 'RAVE'
    (Magnotti J.F., Wang Z., Beauchamp M.S. (2020), R analysis 
    and visualizations of 'iEEG' <doi:10.1016/j.neuroimage.2020.117341>). 
    Provides infrastructure to integrate customized analysis pipelines into
    dashboard modules, including file structures, front-end widgets, and 
    event handlers.
	"""
	
	homepage = "https://dipterix.org/ravedash/"
	cran = "ravedash" 

	version("0.1.2", md5="c02d36b0c13a2a0f4728d79f0ee5f464")

	depends_on("r-dipsaus@0.2:", type=("build", "run"))
	depends_on("r-logger@0.2.2:", type=("build", "run"))
	depends_on("r-raveio@0.0.6:", type=("build", "run"))
	depends_on("r-rpymat@0.1.2:", type=("build", "run"))
	depends_on("r-shidashi@0.1.1:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-shinywidgets@0.6.2:", type=("build", "run"))
	depends_on("r-threebrain@0.2.4:", type=("build", "run"))
	depends_on("r-shinyvalidate", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
