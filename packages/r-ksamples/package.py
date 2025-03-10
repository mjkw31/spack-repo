# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKsamples(RPackage):
	"""K-Sample Rank Tests and their Combinations.

	Compares k samples using the Anderson-Darling test, Kruskal-Wallis type
	tests with different rank score criteria, Steel's multiple comparison test,
	and the Jonckheere-Terpstra (JT) test. It computes asymptotic, simulated or
	(limited) exact P-values, all valid under randomization, with or without
	ties, or conditionally under random sampling from populations, given the
	observed tie pattern. Except for Steel's test and the JT test it also
	combines these tests across several blocks of samples. Also analyzed are 2
	x t contingency tables and their blocked combinations using the
	Kruskal-Wallis criterion. Steel's test is inverted to provide simultaneous
	confidence bounds for shift parameters. A plotting function compares tail
	probabilities obtained under asymptotic approximation with those obtained
	via simulation or exact calculations."""

	cran = "kSamples"

	version("1.2-10", md5="b3f45e87748adf618c76c59740fcf3f7")

	depends_on("r-suppdists", type=("build", "run"))
