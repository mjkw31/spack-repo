# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsych(RPackage):
	"""Procedures for Psychological, Psychometric, and Personality Research.

	A general purpose toolbox for personality, psychometric theory and
	experimental psychology. Functions are primarily for multivariate analysis
	and scale construction using factor analysis, principal component analysis,
	cluster analysis and reliability analysis, although others provide basic
	descriptive statistics. Item Response Theory is done using factor analysis
	of tetrachoric and polychoric correlations.  Functions for analyzing data
	at multiple levels include within and between group statistics, including
	correlations and factor analysis.  Functions for simulating and testing
	particular item and test structures are included. Several functions serve
	as a useful front end for structural equation modeling. Graphical displays
	of path diagrams, factor analysis and structural equation models are
	created using basic graphics. Some of the functions are written to support
	a book on psychometric theory as well as publications in personality
	research.  For more information, see the <http://personality-project.org/r>
	web page."""

	cran = "psych"

	version("2.4.1", md5="43b4e982093c44266b3ed8e18902b916")

	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
