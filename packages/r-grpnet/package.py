# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrpnet(RPackage):
	"""Group Elastic Net Regularized GLM

	Efficient algorithms for fitting generalized linear models with group elastic net penalties. Implements group lasso, group MCP, and group SCAD with an optional group ridge penalty. Computes the regularization path for linear regression (gaussian), logistic regression (binomial), multinomial logistic regression (multinomial), log-linear count regression (poisson and negative.binomial), and log-linear continuous regression (gamma and inverse gaussian). Supports default and formula methods for model specification, k-fold cross-validation for tuning the regularization parameters, and nonparametric regression via tensor product reproducing kernel (smoothing spline) basis function expansion. 
	"""
	
	cran = "grpnet" 

	version("0.2", md5="055f776b1be89a2e72910703b145c2c9")

	depends_on("r@3.5:", type=("build", "run"))
