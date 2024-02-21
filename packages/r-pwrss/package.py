# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwrss(RPackage):
	"""Statistical Power and Sample Size Calculation Tools

	Statistical power and minimum required sample size calculations for (1) testing a proportion (one-sample) against a constant,  (2) testing a mean (one-sample) against a constant,  (3) testing difference between two proportions (independent samples),  (4) testing difference between two means or groups (parametric and non-parametric tests for independent and paired samples),  (5) testing a correlation (one-sample) against a constant,  (6) testing difference between two correlations (independent samples), (7) testing a single coefficient in multiple linear regression, logistic regression, and Poisson regression (with standardized or unstandardized coefficients, with no covariates or covariate adjusted), (8) testing an indirect effect (with standardized or unstandardized coefficients, with no covariates or covariate adjusted) in the mediation analysis (Sobel, Joint, and Monte Carlo tests), (9) testing an R-squared against zero in linear regression, (10) testing an R-squared difference against zero in hierarchical regression,  (11) testing an eta-squared or f-squared (for main and interaction effects) against zero in analysis of variance (could be one-way, two-way, and three-way),  (12) testing an eta-squared or f-squared (for main and interaction effects) against zero in analysis of covariance (could be one-way, two-way, and three-way),  (13) testing an eta-squared or f-squared (for between, within, and interaction effects) against zero in one-way repeated measures analysis of variance (with non-sphericity correction and repeated measures correlation), and (14) testing goodness-of-fit or independence for contingency tables. Alternative hypothesis can be formulated as "not equal", "less", "greater", "non-inferior", "superior", or "equivalent" in (1), (2), (3), and (4); as "not equal", "less", or "greater" in (5), (6), (7) and (8); but always as "greater" in (9), (10), (11), (12), (13), and (14). Reference: Bulus and Polat (2023) <https://osf.io/ua5fc>.
	"""
	
	cran = "pwrss" 

	version("0.3.1", md5="9be7aaeb604a18bc070f00bf415029ac")

