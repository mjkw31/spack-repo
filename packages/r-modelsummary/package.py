# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelsummary(RPackage):
	"""Summary Tables and Plots for Statistical Models and Data:
Beautiful, Customizable, and Publication-Ready

	Create beautiful and customizable tables to summarize several
    statistical models side-by-side. Draw coefficient plots, multi-level
    cross-tabs, dataset summaries, balance tables (a.k.a. "Table 1s"), and
    correlation matrices. This package supports dozens of statistical models, and
    it can produce tables in HTML, LaTeX, Word, Markdown, PDF, PowerPoint, Excel,
    RTF, JPG, or PNG. Tables can easily be embedded in 'Rmarkdown' or 'knitr'
    dynamic documents. Details can be found in Arel-Bundock (2022)
    <doi:10.18637/jss.v103.i01>.
	"""
	
	homepage = "https://modelsummary.com"
	cran = "modelsummary" 

	version("1.4.3", md5="72460d5d96532a7d43c834b42ba35090")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-kableextra@1.3.4:", type=("build", "run"))
	depends_on("r-insight@0.19.6:", type=("build", "run"))
	depends_on("r-parameters@0.21.2:", type=("build", "run"))
	depends_on("r-performance@0.10.5:", type=("build", "run"))
	depends_on("r-tables@0.9.17:", type=("build", "run"))
