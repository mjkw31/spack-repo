# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStagedtrees(RPackage):
	"""Staged Event Trees

	Creates and fits staged event tree probability models,
             which are probabilistic graphical models capable of representing
             asymmetric conditional independence statements
             for categorical variables.
             Includes functions to create, plot and fit staged
             event trees from data, as well as many efficient structure
             learning algorithms.
             References:
             Carli F, Leonelli M, Riccomagno E, Varando G (2022).
             <doi: 10.18637/jss.v102.i06>.
             Collazo R. A., Görgen C. and Smith J. Q.
             (2018, ISBN:9781498729604).
             Görgen C., Bigatti A., Riccomagno E. and Smith J. Q. (2018)
             <arXiv:1705.09457>.
             Thwaites P. A., Smith, J. Q. (2017) <arXiv:1510.00186>.
             Barclay L. M., Hutton J. L. and Smith J. Q. (2013)
             <doi:10.1016/j.ijar.2013.05.006>.
             Smith J. Q. and Anderson P. E. (2008)
             <doi:10.1016/j.artint.2007.05.004>.
	"""
	
	homepage = "https://github.com/stagedtrees/stagedtrees"
	cran = "stagedtrees" 

	version("2.3.0", md5="06b2f1ad6be46854ae00a56e5df1cf04")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
