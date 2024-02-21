# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTargets(RPackage):
	"""Dynamic Function-Oriented 'Make'-Like Declarative Pipelines

	Pipeline tools coordinate the pieces of computationally
  demanding analysis projects.
  The 'targets' package is a 'Make'-like pipeline tool for statistics and
  data science in R. The package skips costly runtime for tasks
  that are already up to date,
  orchestrates the necessary computation with implicit parallel computing,
  and abstracts files as R objects. If all the current output matches
  the current upstream code and data, then the whole pipeline is up
  to date, and the results are more trustworthy than otherwise.
  The methodology in this package
  borrows from GNU 'Make' (2015, ISBN:978-9881443519)
  and 'drake' (2018, <doi:10.21105/joss.00550>).
	"""
	
	homepage = "https://docs.ropensci.org/targets/"
	cran = "targets" 

	version("1.4.1", md5="5c23e615c27e8227e4fc26cd652ceea1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-base64url@1.4:", type=("build", "run"))
	depends_on("r-callr@3.7:", type=("build", "run"))
	depends_on("r-cli@2.0.2:", type=("build", "run"))
	depends_on("r-codetools@0.2.16:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-digest@0.6.25:", type=("build", "run"))
	depends_on("r-igraph@1.2.5:", type=("build", "run"))
	depends_on("r-knitr@1.34:", type=("build", "run"))
	depends_on("r-r6@2.4.1:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-vctrs@0.2.4:", type=("build", "run"))
	depends_on("r-yaml@2.2.1:", type=("build", "run"))
