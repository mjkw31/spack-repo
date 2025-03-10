# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmcmrplus(RPackage):
	"""Calculate Pairwise Multiple Comparisons of Mean Rank Sums Extended.

	For one-way layout experiments the one-way ANOVA can be performed as an
	omnibus test. All-pairs multiple comparisons tests (Tukey-Kramer test,
	Scheffe test, LSD-test) and many-to-one tests (Dunnett test) for normally
	distributed residuals and equal within variance are available. Furthermore,
	all-pairs tests (Games-Howell test, Tamhane's T2 test, Dunnett T3 test,
	Ury-Wiggins-Hochberg test) and many-to-one (Tamhane-Dunnett Test) for
	normally distributed residuals and heterogeneous variances are provided.
	Van der Waerden's normal scores test for omnibus, all-pairs and many-to-one
	tests is provided for non-normally distributed residuals and homogeneous
	variances. The Kruskal-Wallis, BWS and Anderson-Darling omnibus test and
	all-pairs tests (Nemenyi test, Dunn test, Conover test,
	Dwass-Steele-Critchlow- Fligner test) as well as many-to-one (Nemenyi test,
	Dunn test, U-test) are given for the analysis of variance by ranks.
	Non-parametric trend tests (Jonckheere test, Cuzick test, Johnson-Mehrotra
	test, Spearman test) are included.  In addition, a Friedman-test for
	one-way ANOVA with repeated measures on ranks (CRBD) and Skillings-Mack
	test for unbalanced CRBD is provided with consequent all-pairs tests
	(Nemenyi test, Siegel test, Miller test, Conover test, Exact test) and
	many-to-one tests (Nemenyi test, Demsar test, Exact test).  A trend can be
	tested with Pages's test. Durbin's test for a two-way balanced incomplete
	block design (BIBD) is given in this package as well as Gore's test for
	CRBD with multiple observations per cell is given.  Outlier tests, Mandel's
	k- and h statistic as well as functions for Type I error and Power analysis
	as well as generic summary, print and plot methods are provided."""

	cran = "PMCMRplus"

	version("1.9.10", md5="8add406582b95d29df406d61089b0d00")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm@1:", type=("build", "run"))
	depends_on("r-multcompview", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
	depends_on("r-ksamples@1.2.7:", type=("build", "run"))
	depends_on("r-bwstest@0.2.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("gmp@3.2.3:", type=("build", "link", "run"))
	depends_on("mpfr@3.0.0:", type=("build", "link", "run"))
