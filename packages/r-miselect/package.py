# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiselect(RPackage):
	"""Variable Selection for Multiply Imputed Data

	
    Penalized regression methods, such as lasso and elastic net, are used in
    many biomedical applications when simultaneous regression coefficient
    estimation and variable selection is desired. However, missing data
    complicates the implementation of these methods, particularly when
    missingness is handled using multiple imputation. Applying a variable
    selection algorithm on each imputed dataset will likely lead
    to different sets of selected predictors, making it difficult
    to ascertain a final active set without resorting to ad hoc
    combination rules. 'miselect' presents Stacked Adaptive Elastic Net (saenet)
    and Grouped Adaptive LASSO (galasso) for continuous and binary outcomes,
    developed by Du et al (2020), currently under review. They, by construction,
    force selection of the same variables across multiply imputed data.
    'miselect' also provides cross validated variants of these methods.
	"""
	
	cran = "miselect" 

	version("0.9.0", md5="64b6bc1bd49f8af372ac95234f2c4060")

	depends_on("r@3.5:", type=("build", "run"))
